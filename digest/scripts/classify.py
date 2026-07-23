"""Stage 3. Classification and bullet writing, done by the routine session.

There is no API key in this pipeline. The Claude Code session that runs the
routine is the model. This script has two modes:

  prepare  writes batches of records as readable markdown for the session
  apply    validates the session's JSON answers and merges them back

Between the two, the session reads data/runs/edition-NNN/batch-K.md, thinks,
and writes data/runs/edition-NNN/batch-K.answer.json. The rubric lives in
prompts/classify.md.

Usage:
  python3 scripts/classify.py prepare --edition 12 --batch-size 8
  python3 scripts/classify.py apply   --edition 12
"""

import argparse
import glob
import json
import os

from common import CFG, ROOT, log, read_json, write_json

FIELDS = [f["id"] for f in CFG["taxonomy"]["fields"]]
ROLES = [r["id"] for r in CFG["taxonomy"]["roles"]]
PROVENANCE = ["author", "editor", "ai", "none"]


def load_overrides():
    """Author-submitted and editor-written bullets win over generated ones."""
    import yaml
    out = {}
    for name, prov in (("submissions.yaml", "author"), ("overrides.yaml", "editor")):
        path = os.path.join(ROOT, "data", name)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        for entry in doc.get("entries", []) or []:
            key = (entry.get("doi") or entry.get("arxiv_id") or "").lower().strip()
            if key and entry.get("bullets"):
                out[key] = {"bullets": entry["bullets"][:3], "provenance": prov, "meta": entry}
    return out


def prepare(args):
    run_dir = os.path.join(ROOT, "data", "runs", "edition-%03d" % args.edition)
    recs = read_json(os.path.join(run_dir, "enriched.json"), [])
    if not recs:
        raise SystemExit("No enriched.json for edition %d" % args.edition)

    overrides = load_overrides()
    todo = []
    for r in recs:
        key = (r.get("doi") or r.get("arxiv_id") or "").lower()
        if key in overrides:
            r["bullets"] = overrides[key]["bullets"]
            r["bullet_provenance"] = overrides[key]["provenance"]
        else:
            todo.append(r)

    write_json(os.path.join(run_dir, "with_overrides.json"), recs)
    for old in glob.glob(os.path.join(run_dir, "batch-*.md")):
        os.remove(old)

    size = args.batch_size
    batches = [todo[i:i + size] for i in range(0, len(todo), size)]
    for bi, batch in enumerate(batches, start=1):
        lines = [
            "# Classification batch %d of %d, edition %d" % (bi, len(batches), args.edition),
            "",
            "Read prompts/classify.md before answering. Write your answer to",
            "`data/runs/edition-%03d/batch-%d.answer.json` as a JSON array." % (args.edition, bi),
            "",
            "---",
            "",
        ]
        for rec in batch:
            lines += [
                "## uid: `%s`" % rec["uid"],
                "",
                "- title: %s" % rec["title"],
                "- authors: %s" % (", ".join(rec["authors"][:8]) or "not stated"),
                "- affiliations: %s" % (", ".join(rec["affiliations"][:6]) or "not stated"),
                "- posted: %s" % (rec.get("posted") or "not stated"),
                "- source: %s" % rec.get("source_label", ""),
                "- link: %s" % rec.get("url", ""),
                "- keyword hits: %s" % (", ".join(rec.get("matched_terms", [])) or "none"),
                "",
                "### abstract",
                "",
                (rec.get("abstract") or "NOT AVAILABLE. You have title and authors only. "
                 "Set bullet_provenance to \"none\", return an empty bullets array, and "
                 "classify field and role only if the title makes it unambiguous."),
                "",
                "---",
                "",
            ]
        with open(os.path.join(run_dir, "batch-%d.md" % bi), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))

    log("Prepared %d batches covering %d records. %d already have author or editor bullets."
        % (len(batches), len(todo), len(recs) - len(todo)))
    write_json(os.path.join(run_dir, "batch-manifest.json"),
               {"batches": len(batches), "to_classify": len(todo), "pre_filled": len(recs) - len(todo)})


def validate(ans, uid_set):
    """Reject anything malformed. A bad batch is re-done, never guessed at."""
    problems = []
    if ans.get("uid") not in uid_set:
        problems.append("unknown uid %s" % ans.get("uid"))
    if ans.get("field") not in FIELDS:
        problems.append("bad field %s" % ans.get("field"))
    if ans.get("role") not in ROLES:
        problems.append("bad role %s" % ans.get("role"))
    prov = ans.get("bullet_provenance")
    if prov not in PROVENANCE:
        problems.append("bad provenance %s" % prov)
    bullets = ans.get("bullets") or []
    if prov == "none":
        if bullets:
            problems.append("provenance none must have zero bullets")
    else:
        if len(bullets) != 3:
            problems.append("expected 3 bullets, got %d" % len(bullets))
        for b in bullets:
            if not isinstance(b, str) or len(b.split()) > 45:
                problems.append("bullet too long or not a string")
    if not isinstance(ans.get("salience", 0), (int, float)):
        problems.append("salience not numeric")
    return problems


def apply_(args):
    run_dir = os.path.join(ROOT, "data", "runs", "edition-%03d" % args.edition)
    recs = read_json(os.path.join(run_dir, "with_overrides.json"), [])
    if not recs:
        raise SystemExit("No with_overrides.json. Run prepare first.")
    by_uid = {r["uid"]: r for r in recs}

    answers, bad = [], []
    for path in sorted(glob.glob(os.path.join(run_dir, "batch-*.answer.json"))):
        try:
            payload = json.load(open(path, "r", encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            bad.append("%s is not valid JSON: %s" % (os.path.basename(path), exc))
            continue
        if not isinstance(payload, list):
            bad.append("%s is not a JSON array" % os.path.basename(path))
            continue
        answers.extend(payload)

    applied = 0
    for ans in answers:
        problems = validate(ans, set(by_uid))
        if problems:
            bad.append("%s: %s" % (ans.get("uid", "?"), "; ".join(problems)))
            continue
        rec = by_uid[ans["uid"]]
        rec["field"] = ans["field"]
        rec["role"] = ans["role"]
        rec["bullets"] = ans.get("bullets") or []
        rec["bullet_provenance"] = ans["bullet_provenance"]
        rec["validated"] = ans.get("validated")
        rec["validation_note"] = (ans.get("validation_note") or "")[:200]
        rec["salience"] = int(ans.get("salience") or 0)
        if ans.get("models"):
            rec["models"] = sorted(set(rec.get("models", []) + list(ans["models"])))
        if ans.get("open_weights") is not None:
            rec["open_weights"] = bool(ans["open_weights"])
        if ans.get("drop"):
            rec["flags"] = sorted(set(rec.get("flags", []) + ["dropped_by_classifier"]))
        applied += 1

    classified = [r for r in recs if r.get("field") and r.get("role")
                  and "dropped_by_classifier" not in r.get("flags", [])]

    log("Applied %d answers. %d records classified. %d rejected." % (applied, len(classified), len(bad)))
    for b in bad[:25]:
        log("  REJECTED %s" % b)

    unclassified = [r["uid"] for r in recs if not r.get("field")
                    and "dropped_by_classifier" not in r.get("flags", [])]
    if unclassified:
        log("Still unclassified (%d). Re-run those batches before building:" % len(unclassified))
        for u in unclassified[:15]:
            log("  %s" % u)

    write_json(os.path.join(run_dir, "classified.json"), classified)
    write_json(os.path.join(run_dir, "rejects.json"), {"rejected": bad, "unclassified": unclassified})


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--edition", type=int, required=True)
    p.add_argument("--batch-size", type=int, default=8)
    p.set_defaults(fn=prepare)
    a = sub.add_parser("apply")
    a.add_argument("--edition", type=int, required=True)
    a.set_defaults(fn=apply_)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
