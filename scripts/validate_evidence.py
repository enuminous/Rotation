"""Validate cross-field evidence IDs, source integrity and epistemic labels."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root: Path = ROOT) -> dict[str, object]:
    registry = json.loads((root / "data" / "evidence.json").read_text(encoding="utf-8"))
    references = json.loads((root / "data" / "sources.json").read_text(encoding="utf-8"))
    sources = references["sources"]
    claims = registry["evidence"]
    vocabulary = set(registry["status_vocabulary"])
    ids = [r["id"] for r in sources]
    claim_ids = [c["id"] for c in claims]
    assert len(ids) == len(set(ids)), "duplicate source ID"
    assert len(claim_ids) == len(set(claim_ids)), "duplicate claim ID"
    assert len(claims) >= 20 and len(sources) >= 15, "unexpectedly small corpus"
    for src in sources:
        assert src["id"] and src["url"].startswith("https://"), "malformed source"
        assert src["title"] and src["type"], "source missing description"
    for c in claims:
        assert c["status"] in vocabulary, f"unknown evidence status {c['id']}"
        assert c["claim"] and c["description"] and c["domain"], f"empty claim {c['id']}"
        assert c["limits"].strip() and c["relevance_to_global_rotation"], f"unqualified claim {c['id']}"
        assert c["source_ids"], f"uncited claim {c['id']}"
        assert all(s in ids for s in c["source_ids"]), f"invalid citation {c['id']}"
    counts = {status: sum(1 for c in claims if c["status"] == status)
              for status in sorted(vocabulary)}
    return {"status": "PASS_SCHEMA_AND_CITATIONS", "claims": len(claims),
            "sources": len(sources), "status_counts": counts,
            "warning": "This checks internal registry consistency, NOT publication accuracy or scientific validation."}


def main() -> None:
    print(json.dumps(validate(), indent=2))


if __name__ == "__main__":
    main()
