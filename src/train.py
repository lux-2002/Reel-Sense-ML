"""End-to-end training entry point for ReelSense.

This script is intentionally conservative: it validates the dataset and feature
contract before training. Model selection belongs in the development notebook,
then the winning validated pipeline can be moved here for reproducible training.
"""

from pathlib import Path
import pandas as pd

from preprocessing import TARGET, validate_feature_contract

DATA_PATH = Path("data/Rotten_Tomatoes_Movies3.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Add Rotten_Tomatoes_Movies3.csv to data/."
        )
    return pd.read_csv(path)


def validate_data(df: pd.DataFrame) -> None:
    validate_feature_contract()
    if TARGET not in df.columns:
        raise ValueError(f"Required target column missing: {TARGET}")


if __name__ == "__main__":
    df = load_data()
    validate_data(df)
    print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.")
    print(f"Target missing values: {df[TARGET].isna().sum():,}")
    print("Next step: run notebooks/02_model_development.ipynb.")
