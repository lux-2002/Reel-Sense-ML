# Project Evolution

## 1. Original Zoho assessment

The original project was developed as a Zoho machine-learning assessment titled **Predicting Audience Ratings for Movies**.

The original workflow explored a Rotten Tomatoes dataset, used mixed numerical/categorical information, experimented with Random Forest regression and referenced text processing through TF-IDF.

## 2. Methodology audit

The original implementation is preserved conceptually as the starting point, but several areas require correction before it can be presented as a polished ML project:

- `audience_rating` must never be present among predictors.
- Target values should not be casually imputed using test-set statistics.
- Preprocessing must be learned only from training data/folds.
- OneHotEncoder/OrdinalEncoder choices should be deliberate and consistent.
- TF-IDF must be integrated into the real modelling pipeline rather than demonstrated on one sample.
- Hyperparameter optimization should only be claimed when it is actually performed.
- Regression should be evaluated with MAE, RMSE and R².
- Notebook package installation commands should be replaced by `requirements.txt`.

## 3. Rebuild

The rebuilt project separates data exploration, feature engineering, training and evaluation. The goal is reproducibility and methodological clarity rather than unnecessary software architecture.

## 4. Experimentation

The experiment plan compares feature groups:

| Experiment | Feature family | Purpose |
|---|---|---|
| Baseline | Numeric | Establish a simple reference |
| Metadata | Numeric + categorical | Measure structured movie information |
| Text | Metadata + TF-IDF | Measure language contribution |
| Final | Selected engineered features | Validate the strongest justified pipeline |

Actual metrics belong in the experiment notebooks only after execution.

## 5. Product layer

ReelSense turns the resulting model into a movie-discovery experience. The eventual application should clearly distinguish:

- **Actual audience rating** from the dataset
- **Critic rating** from the dataset
- **Predicted audience signal** produced by the model
- Any uncertainty/confidence measure, only if the final modelling approach supports one

The website must never present an unexecuted model score as a real prediction.
