#!/usr/bin/env python3
"""Basic repository health check utility."""

from __future__ import annotations

from pathlib import Path
import json


def evaluate_repo(root: Path) -> dict:
    expected = ["README.md", "src", "tests", "configs", "docs"]
    present = {}
    for item in expected:
        target = root / item
        present[item] = target.exists()

    missing = [item for item, ok in present.items() if not ok]
    score = int(((len(expected) - len(missing)) / len(expected)) * 100)

    return {
        "repository": root.name,
        "score": score,
        "present": present,
        "missing": missing,
        "status": "healthy" if score >= 80 else "needs_attention",
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    report = evaluate_repo(root)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

# Health check validated against Python 3.11 – March 2026
# Health check validated against Python 3.11 – March 2026 – 2026-03-08 22:57:37 [84a21a7d]
# Health check validated against Python 3.11 – March 2026 – 2026-03-08 22:58:28 [48b2f4c2]
# Health check validated against Python 3.11 – March 2026 – 2026-03-08 23:00:17 [3f39de2c]
# Health check validated against Python 3.11 – March 2026 – 2026-03-10 09:17:58 [20e7005f]
