"""Build reproducibility manifests for experiment runs."""

import hashlib
from datetime import datetime, timezone

from src.repro.fingerprint import params_fingerprint


def manifest_signature(pipeline_version: str, data_version: str, params_fp: str) -> str:
    payload = f"{pipeline_version}|{data_version}|{params_fp}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_manifest(params: dict, pipeline_version: str, data_version: str) -> dict[str, str]:
    params_fp = params_fingerprint(params)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_version": pipeline_version,
        "data_version": data_version,
        "params_fingerprint": params_fp,
        "manifest_signature": manifest_signature(pipeline_version, data_version, params_fp),
    }


def has_required_manifest_fields(manifest: dict[str, str]) -> bool:
    required = {
        "generated_at",
        "pipeline_version",
        "data_version",
        "params_fingerprint",
        "manifest_signature",
    }
    return required.issubset(manifest.keys())
