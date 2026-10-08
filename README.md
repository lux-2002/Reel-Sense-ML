# ReelSense 🎬

### Don't just watch. Know the signal.

**ReelSense** is a movie-discovery product built on a Rotten Tomatoes dataset, with a machine-learning layer designed to estimate **audience response** from movie metadata, critic reception and text.

This project began as a **Zoho ML assessment** and is being re-engineered into a reproducible ML project with a polished product-facing movie discovery experience.

## Why this project exists

The original assessment solved a legitimate regression problem, but the first implementation was not yet strong enough to represent production-quality ML work. ReelSense is the deliberate second version: preserve the useful idea, audit the methodology, rebuild the pipeline correctly, and turn the resulting intelligence into a product experience.

## Product experience

The `website/` folder contains the current ReelSense UI: a dark, cinematic movie-discovery interface inspired by modern movie platforms while maintaining its own identity.

The website is designed to grow from a prototype into a data-backed application where the complete movie dataset powers search, filters, movie details and ML-derived audience intelligence.

## ML objective

**Target:** `audience_rating`

The project investigates whether audience response can be estimated from:

- Numerical signals such as runtime and Tomatometer metrics
- Categorical metadata such as genre, directors, writers and studio
- Text from `critics_consensus` and `movie_info`

## Planned end-to-end workflow

1. Load and validate the complete dataset.
2. Audit missing values, duplicates, types and target distribution.
3. Remove target leakage and define a clean feature contract.
4. Build preprocessing inside reproducible scikit-learn pipelines.
5. Establish simple regression baselines.
6. Benchmark tree-based and linear models.
7. Integrate TF-IDF text features properly rather than vectorizing a single example.
8. Compare feature groups through controlled experiments.
9. Use cross-validation and regression metrics.
10. Perform residual/error analysis.
11. Save the final validated model and metrics.
12. Connect model outputs to ReelSense.

## Evaluation

The primary regression metrics are:

- **MAE** — average absolute prediction error
- **RMSE** — penalizes larger errors more strongly
- **R²** — proportion of target variance explained by the model

No performance number is claimed until the rebuilt pipeline has actually been executed on the complete dataset.

## Project evolution

**Zoho Assessment → Methodology Audit → Leakage-Safe Rebuild → Feature Experiments → Model Benchmarking → ReelSense Product**

## Repository structure

```text
ReelSense/
├── website/
│   └── index.html
├── data/
│   └── README.md
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_model_development.ipynb
│   └── 03_model_evaluation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
├── models/
├── reports/
│   └── figures/
├── tests/
│   └── test_preprocessing.py
├── README.md
├── PROJECT_EVOLUTION.md
├── requirements.txt
└── .gitignore
```

## Dataset

Put your complete local dataset here:

`data/Rotten_Tomatoes_Movies3.csv`

The project is designed for the full ~16,639-row dataset. The CSV is intentionally not included in this starter repository so the original file stays under your control and is not accidentally duplicated.

## Tech stack

Python · Pandas · NumPy · Scikit-learn · TF-IDF / NLP · Matplotlib · Seaborn · Jupyter · Joblib · Pytest · HTML · CSS · JavaScript

## Portfolio positioning

This is intentionally more than a notebook dump. The repository demonstrates a progression from an assessment implementation to a methodologically stronger ML pipeline and then to a product-facing experience.

**The notebooks prove the ML. ReelSense is the product.**
