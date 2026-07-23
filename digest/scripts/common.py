"""Shared helpers for the LLM Research Digest pipeline.

The single most important thing in this file is guarded_get(). Every outbound
request in the pipeline goes through it. It refuses to contact any host listed
under blocked_hosts in config.yaml. SSRN's terms of use prohibit automated
querying, so we never touch ssrn.com. SSRN coverage comes from Crossref, which
SSRN deposits to as a Crossref member.
"""

import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

import requests
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config(path=None):
    path = path or os.path.join(ROOT, "config.yaml")
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


CFG = load_config()
BLOCKED = set(h.lower() for h in CFG.get("blocked_hosts", []))


class BlockedHostError(RuntimeError):
    pass


def guarded_get(url, params=None, headers=None, timeout=None, retries=None):
    """HTTP GET that refuses blocked hosts and retries with backoff."""
    host = (urlparse(url).hostname or "").lower()
    if host in BLOCKED or any(host.endswith("." + b) for b in BLOCKED):
        raise BlockedHostError(
            "Refusing to contact %s. It is on the blocked_hosts list. "
            "Use Crossref or OpenAlex for this publisher's metadata." % host
        )
    run = CFG["run"]
    timeout = timeout or run["request_timeout"]
    retries = retries or run["retries"]
    hdrs = {"User-Agent": run["user_agent"], "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    last = None
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, headers=hdrs, timeout=timeout)
            if resp.status_code == 429:
                time.sleep(run["backoff_seconds"] * (attempt + 2))
                continue
            resp.raise_for_status()
            return resp
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(run["backoff_seconds"] * (attempt + 1))
    raise RuntimeError("GET failed after %d attempts: %s (%s)" % (retries, url, last))


def window(days=None):
    days = days or CFG["run"]["window_days"]
    end = datetime.now(timezone.utc).date()
    return (end - timedelta(days=days)).isoformat(), end.isoformat()


def norm_title(title):
    if not title:
        return ""
    t = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9 ]+", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def strip_tags(text):
    if not text:
        return ""
    # Crossref sometimes delivers HTML-entity-encoded tags (e.g. &lt;p&gt;),
    # so unescape and strip repeatedly until stable, then collapse whitespace.
    import html as _html
    text = str(text)
    for _ in range(3):
        new = re.sub(r"<[^>]+>", " ", _html.unescape(text))
        if new == text:
            break
        text = new
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def blank_record():
    return {
        "uid": "",
        "doi": "",
        "arxiv_id": "",
        "title": "",
        "authors": [],
        "affiliations": [],
        "posted": "",
        "source_label": "",
        "source_id": "",
        "url": "",
        "abstract": "",
        "abstract_source": "",
        "relevance": 0,
        "matched_terms": [],
        # filled by the classifier
        "field": "",
        "role": "",
        "bullets": [],
        "bullet_provenance": "none",
        "models": [],
        "open_weights": None,
        "validated": None,
        "validation_note": "",
        "salience": 0,
        "flags": [],
    }


def make_uid(rec):
    if rec.get("doi"):
        return "doi:" + rec["doi"].lower()
    if rec.get("arxiv_id"):
        return "arxiv:" + rec["arxiv_id"].lower()
    return "title:" + norm_title(rec.get("title", ""))[:120]


def score_relevance(rec, cfg=None):
    """Stage 1 gate. Cheap substring matching over title plus abstract."""
    cfg = cfg or CFG
    kw = cfg["keywords"]
    hay = (" " + (rec.get("title") or "") + " " + (rec.get("abstract") or "") + " ").lower()
    hay = re.sub(r"[^a-z0-9\- ]+", " ", hay)

    for bad in kw.get("exclude", []):
        if bad in hay:
            return 0, []

    hits, score = [], 0
    for term in kw.get("strong", []):
        if term in hay:
            hits.append(term.strip())
            score += 2
    for term in kw.get("weak", []):
        if term in hay:
            hits.append(term.strip())
            score += 1
    if cfg["keywords"].get("include_legacy_nlp"):
        for term in kw.get("legacy_nlp", []):
            if term in hay:
                hits.append(term.strip())
                score += 1

    if score == 0:
        return 0, []

    if any(d in hay for d in cfg.get("domain_terms", [])):
        score += 1
    else:
        score -= 1

    return max(score, 0), sorted(set(hits))


def detect_models(text, cfg=None):
    cfg = cfg or CFG
    low = (text or "").lower()
    fams = []
    for fam, terms in cfg.get("model_families", {}).items():
        if any(t in low for t in terms):
            fams.append(fam)
    return sorted(set(fams))


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def append_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def read_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def log(msg):
    print(msg, flush=True)


def die(msg, code=1):
    print("FATAL: " + msg, file=sys.stderr, flush=True)
    sys.exit(code)
