from src.preprocessing import TARGET, NUMERICAL_FEATURES, CATEGORICAL_FEATURES, TEXT_FEATURES, validate_feature_contract


def test_target_is_not_a_feature():
    assert TARGET not in NUMERICAL_FEATURES
    assert TARGET not in CATEGORICAL_FEATURES
    assert TARGET not in TEXT_FEATURES


def test_feature_contract_is_valid():
    validate_feature_contract()
