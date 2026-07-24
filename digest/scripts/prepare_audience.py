"""Prepare audience-tagging batches for papers that lack an `audience` tag.

Judges technical-vs-general from our own published bullets (no abstracts), so
the batch files carry only public metadata. Writes to data/runs/edition-003/aud/.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(ROOT, "data", "index.jsonl")
AUD = os.path.join(ROOT, "data", "runs", "edition-003", "aud")
BATCH = 15


def main():
    recs = []
    with open(IDX, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    todo = [r for r in recs if "audience" not in r]
    print("Records total %d. Need audience tag: %d." % (len(recs), len(todo)))

    os.makedirs(AUD, exist_ok=True)
    for old in os.listdir(AUD):
        os.remove(os.path.join(AUD, old))

    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    for bi, batch in enumerate(batches, start=1):
        lines = [
            "# Audience batch %d of %d" % (bi, len(batches)),
            "",
            "For each paper decide if it is TECHNICAL or GENERAL for a business /",
            "finance / economics / accounting audience, judging from the summary.",
            "Write your answer to `aud/batch-%d.answer.json` as a JSON array." % bi,
            "",
            "---",
            "",
        ]
        for r in batch:
            bullets = r.get("bullets") or []
            lines += [
                "## uid: `%s`" % r["uid"],
                "",
                "- title: %s" % r.get("title", ""),
                "- field: %s | role: %s" % (r.get("field", ""), r.get("role", "")),
                "- models: %s" % (", ".join(r.get("models", [])) or "none named"),
                "- summary:",
            ]
            if bullets:
                lines += ["  - %s" % b for b in bullets]
            else:
                lines += ["  - (no summary available; judge from the title)"]
            lines += ["", "---", ""]
        with open(os.path.join(AUD, "batch-%d.md" % bi), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))

    print("Wrote %d audience batches to %s" % (len(batches), AUD))
    with open(os.path.join(AUD, "manifest.json"), "w") as fh:
        json.dump({"batches": len(batches), "papers": len(todo)}, fh)


if __name__ == "__main__":
    main()
