"""Build reproducibility manifests for experiment runs."""

from datetime import datetime, timezone

from src.repro.fingerprint import params_fingerprint


def build_manifest(params: dict, pipeline_version: str, data_version: str) -> dict[str, str]:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_version": pipeline_version,
        "data_version": data_version,
        "params_fingerprint": params_fingerprint(params),
    }
