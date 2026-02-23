from src.repro.fingerprint import params_fingerprint


def test_fingerprint_is_stable_for_same_params() -> None:
    params = {"seed": 42, "trim": True, "k": 31}
    fp1 = params_fingerprint(params)
    fp2 = params_fingerprint({"k": 31, "trim": True, "seed": 42})
    assert fp1 == fp2


def test_fingerprint_changes_with_params() -> None:
    p1 = {"seed": 42}
    p2 = {"seed": 43}
    assert params_fingerprint(p1) != params_fingerprint(p2)
