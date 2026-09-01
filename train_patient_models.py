from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "dataset"

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


# ============================================================
# DIABETES PATIENT MODEL
# ============================================================

DATASET_FILE = (
    DATASET_DIR
    / "diabetes.csv"
)

MODEL_FILE = (
    MODEL_DIR
    / "diabetes_patient_model.joblib"
)


PATIENT_FEATURES = [

    "age",
    "gender",
    "polyuria",
    "polydipsia",
    "sudden_weight_loss",
    "weakness",
    "polyphagia",
    "visual_blurring",
    "obesity",

]


TARGET = "class"


# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 75)
print("     CHRONICCARE AI - PATIENT DIABETES MODEL")
print("=" * 75)


print("\nLoading dataset...")

df = pd.read_csv(
    DATASET_FILE
)


# Remove accidental whitespace from column names

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


print(
    f"Dataset shape: {df.shape}"
)


# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required_columns = (
    PATIENT_FEATURES
    + [TARGET]
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
# CLEAN TEXT VALUES
# ============================================================

for column in [
    "gender",
    "polyuria",
    "polydipsia",
    "sudden_weight_loss",
    "weakness",
    "polyphagia",
    "visual_blurring",
    "obesity",
]:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# ============================================================
# TARGET CONVERSION
# ============================================================

target_mapping = {

    "Positive": 1,

    "Negative": 0,

}


df[TARGET] = (
    df[TARGET]
    .astype(str)
    .str.strip()
    .map(target_mapping)
)


# Remove rows with unknown target values

df = df.dropna(
    subset=[TARGET]
)


df[TARGET] = (
    df[TARGET]
    .astype(int)
)


# ============================================================
# FEATURES
# ============================================================

X = df[PATIENT_FEATURES].copy()

y = df[TARGET].copy()


print(
    f"Patient-friendly features: {len(PATIENT_FEATURES)}"
)

print(
    "\nFeatures:"
)

for index, feature in enumerate(
    PATIENT_FEATURES,
    start=1
):

    print(
        f"{index:02d}. {feature}"
    )


print(
    "\nTarget distribution:"
)

print(
    y.value_counts().to_string()
)


# ============================================================
# FEATURE TYPES
# ============================================================

numeric_features = [

    "age",

]


categorical_features = [

    "gender",
    "polyuria",
    "polydipsia",
    "sudden_weight_loss",
    "weakness",
    "polyphagia",
    "visual_blurring",
    "obesity",

]


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


categorical_pipeline = Pipeline(

    steps=[

        (
            "imputer",
            SimpleImputer(
                strategy="most_frequent"
            )
        ),

        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        ),

    ]

)


preprocessor = ColumnTransformer(

    transformers=[

        (
            "numeric",
            numeric_pipeline,
            numeric_features
        ),

        (
            "categorical",
            categorical_pipeline,
            categorical_features
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
# MODEL TRAINING
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

    print(
        "\nConfusion Matrix:"
    )

    print(
        matrix
    )


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


print("\n" + "=" * 75)

print("BEST PATIENT MODEL")

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
    f"Saved to  : {MODEL_FILE}"
)


# ============================================================
# SAVE REPORT
# ============================================================

report = pd.DataFrame([

    {

        "Disease":
            "diabetes",

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


report_file = (
    REPORT_DIR
    / "diabetes_patient_performance.csv"
)


report.to_csv(
    report_file,
    index=False
)


print(
    f"\nReport saved to: {report_file}"
)


print("\n" + "=" * 75)

print(
    "✅ DIABETES PATIENT MODEL TRAINING COMPLETE"
)

print("=" * 75)