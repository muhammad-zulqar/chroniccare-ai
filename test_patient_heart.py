from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_FILE = (
    BASE_DIR
    / "dataset"
    / "heart_disease.csv"
)

MODEL_DIR = BASE_DIR / "ml_models"

REPORT_DIR = (
    BASE_DIR
    / "documentation"
    / "ml_reports"
)

MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


MODEL_FILE = (
    MODEL_DIR
    / "heart_disease_patient_model.joblib"
)

REPORT_FILE = (
    REPORT_DIR
    / "heart_patient_performance.csv"
)


# ============================================================
# PATIENT FEATURES
# ============================================================

PATIENT_FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
]

TARGET = "num"


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 75)
print("       CHRONICCARE AI - PATIENT HEART MODEL")
print("=" * 75)

print("\nLoading dataset...")

df = pd.read_csv(DATASET_FILE)

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

print(
    f"Dataset shape: {df.shape}"
)


# ============================================================
# VERIFY COLUMNS
# ============================================================

required_columns = (
    PATIENT_FEATURES + [TARGET]
)

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:

    raise ValueError(
        "Missing columns: "
        + ", ".join(missing_columns)
    )


# ============================================================
# CLEAN NUMERIC DATA
# ============================================================

for column in PATIENT_FEATURES:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# TARGET
# ============================================================

df[TARGET] = pd.to_numeric(
    df[TARGET],
    errors="coerce"
)

df = df.dropna(
    subset=[TARGET]
)

# 0 = no disease
# 1,2,3,4 = disease presence

df[TARGET] = (
    df[TARGET] > 0
).astype(int)


# ============================================================
# FEATURES AND TARGET
# ============================================================

X = df[PATIENT_FEATURES].copy()

y = df[TARGET].copy()


print(
    f"\nPatient model features: {len(PATIENT_FEATURES)}"
)

print("\nFeatures:")

for number, feature in enumerate(
    PATIENT_FEATURES,
    start=1
):

    print(
        f"{number:02d}. {feature}"
    )


print("\nTarget distribution:")

print(
    y.value_counts().sort_index().to_string()
)


# ============================================================
# PREPROCESSING
# ============================================================

numeric_pipeline = Pipeline(
    steps=[

        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        ),

        (
            "scaler",
            StandardScaler()
        ),

    ]
)


preprocessor = ColumnTransformer(
    transformers=[

        (
            "numeric",
            numeric_pipeline,
            PATIENT_FEATURES
        ),

    ]
)


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = (
    train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42,

        stratify=y,

    )
)


print(
    f"\nTraining samples: {len(X_train)}"
)

print(
    f"Testing samples : {len(X_test)}"
)


# ============================================================
# CANDIDATE MODELS
# ============================================================

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=2000
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=300,
            random_state=42
        ),

}


# ============================================================
# TRAIN AND COMPARE
# ============================================================

best_pipeline = None

best_model_name = None

best_f1 = -1

best_metrics = None


for model_name, model in models.items():

    print("\n" + "-" * 75)

    print(
        f"Training: {model_name}"
    )

    print("-" * 75)


    pipeline = Pipeline(
        steps=[

            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",
                model
            ),

        ]
    )


    pipeline.fit(
        X_train,
        y_train
    )


    predictions = pipeline.predict(
        X_test
    )


    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )


    print(
        f"Accuracy : {accuracy:.4f}"
    )

    print(
        f"Precision: {precision:.4f}"
    )

    print(
        f"Recall   : {recall:.4f}"
    )

    print(
        f"F1 Score : {f1:.4f}"
    )

    print("\nConfusion Matrix:")

    print(matrix)


    if f1 > best_f1:

        best_f1 = f1

        best_pipeline = pipeline

        best_model_name = model_name

        best_metrics = {

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1 Score": f1,

        }


# ============================================================
# SAVE BEST MODEL
# ============================================================

joblib.dump(
    best_pipeline,
    MODEL_FILE
)


# ============================================================
# SAVE PERFORMANCE REPORT
# ============================================================

report = pd.DataFrame([

    {

        "Disease":
            "heart_disease",

        "Mode":
            "patient",

        "Model":
            best_model_name,

        "Accuracy":
            best_metrics["Accuracy"],

        "Precision":
            best_metrics["Precision"],

        "Recall":
            best_metrics["Recall"],

        "F1 Score":
            best_metrics["F1 Score"],

        "Features":
            len(PATIENT_FEATURES),

        "Training Samples":
            len(X_train),

        "Testing Samples":
            len(X_test),

    }

])


report.to_csv(
    REPORT_FILE,
    index=False
)


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 75)

print("BEST PATIENT HEART MODEL")

print("=" * 75)

print(
    f"Model     : {best_model_name}"
)

print(
    f"Accuracy  : {best_metrics['Accuracy']:.4f}"
)

print(
    f"Precision : {best_metrics['Precision']:.4f}"
)

print(
    f"Recall    : {best_metrics['Recall']:.4f}"
)

print(
    f"F1 Score  : {best_metrics['F1 Score']:.4f}"
)

print(
    f"Features  : {len(PATIENT_FEATURES)}"
)

print(
    f"Model saved: {MODEL_FILE}"
)

print(
    f"Report saved: {REPORT_FILE}"
)

print(
    "\n✅ PATIENT HEART MODEL COMPLETE"
)

print("=" * 75)