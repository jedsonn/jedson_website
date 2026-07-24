"""Apply audience judgments back into the index.

Reads aud/batch-*.answer.json ([{uid, technical}]) and sets each matching
record's `audience` field to "technical" or "general". Rewrites index.jsonl.
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(ROOT, "data", "index.jsonl")
AUD = os.path.join(ROOT, "data", "runs", "edition-003", "aud")


def main():
    verdicts = {}
    bad = 0
    for path in sorted(glob.glob(os.path.join(AUD, "batch-*.answer.json"))):
        try:
            arr = json.load(open(path, encoding="utf-8"))
        except Exception:
            bad += 1
            continue
        if not isinstance(arr, list):
            bad += 1
            continue
        for a in arr:
            uid = a.get("uid")
            if uid and isinstance(a.get("technical"), bool):
                verdicts[uid] = a["technical"]
    print("Collected %d verdicts (%d unreadable files)." % (len(verdicts), bad))

    recs = []
    with open(IDX, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                recs.append(json.loads(line))

    applied = tech = 0
    for r in recs:
        v = verdicts.get(r["uid"])
        if v is None:
            continue
        r["audience"] = "technical" if v else "general"
        applied += 1
        if v:
            tech += 1

    with open(IDX, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    tagged = sum(1 for r in recs if "audience" in r)
    tech_total = sum(1 for r in recs if r.get("audience") == "technical")
    print("Applied %d (%d technical). Index now: %d/%d tagged, %d technical."
          % (applied, tech, tagged, len(recs), tech_total))


if __name__ == "__main__":
    main()
