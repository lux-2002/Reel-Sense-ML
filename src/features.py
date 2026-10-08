"""Feature engineering utilities for the ReelSense ML pipeline."""

import pandas as pd


def combine_text_columns(df: pd.DataFrame, columns: list[str]) -> pd.Series:
    """Combine selected text columns safely for downstream TF-IDF."""
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise KeyError(f"Missing text columns: {missing}")
    return df[columns].fillna("").astype(str).agg(" ".join, axis=1)


def drop_rows_without_target(df: pd.DataFrame, target: str = "audience_rating") -> pd.DataFrame:
    """Remove rows without a known target before train/test splitting."""
    return df.dropna(subset=[target]).copy()
