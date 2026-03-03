from src.repro.fingerprint import params_fingerprint
from src.repro.manifest import build_manifest, has_required_manifest_fields, manifest_signature


def test_fingerprint_is_stable_for_same_params() -> None:
    params = {"seed": 42, "trim": True, "k": 31}
    fp1 = params_fingerprint(params)
    fp2 = params_fingerprint({"k": 31, "trim": True, "seed": 42})
    assert fp1 == fp2


def test_fingerprint_changes_with_params() -> None:
    p1 = {"seed": 42}
    p2 = {"seed": 43}
    assert params_fingerprint(p1) != params_fingerprint(p2)


def test_manifest_signature_stability() -> None:
    sig1 = manifest_signature("1.0.0", "dataset-v1", "abc123")
    sig2 = manifest_signature("1.0.0", "dataset-v1", "abc123")
    assert sig1 == sig2


def test_build_manifest_has_required_fields() -> None:
    manifest = build_manifest({"seed": 42}, pipeline_version="1.2.0", data_version="d202603")
    assert has_required_manifest_fields(manifest) is True
