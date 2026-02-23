"""Generate deterministic fingerprints for run parameters."""

import hashlib
import json


def params_fingerprint(params: dict) -> str:
    canonical = json.dumps(params, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
