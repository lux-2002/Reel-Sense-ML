"""Reusable, leakage-safe feature definitions for ReelSense."""

TARGET = "audience_rating"

NUMERICAL_FEATURES = [
    "runtime_in_minutes",
    "tomatometer_rating",
    "tomatometer_count",
]

CATEGORICAL_FEATURES = [
    "genre",
    "directors",
    "writers",
    "studio_name",
]

TEXT_FEATURES = [
    "critics_consensus",
    "movie_info",
]


def validate_feature_contract():
    """Fail fast if the target accidentally enters the numeric feature list."""
    if TARGET in NUMERICAL_FEATURES + CATEGORICAL_FEATURES + TEXT_FEATURES:
        raise ValueError("Target leakage detected: audience_rating is a feature.")
