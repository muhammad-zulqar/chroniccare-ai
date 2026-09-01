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

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_FILE = (
    BASE_DIR
    / "dataset"
    / "liver_patient_symptoms.csv"
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
    / "liver_patient_model.joblib"
)

REPORT_FILE = (
    REPORT_DIR
    / "liver_patient_performance.csv"
)


# ============================================================
# FEATURES
# ============================================================

PATIENT_FEATURES = [

    "Age",
    "Sex",
    "Fatigue",
    "Malaise",
    "Anorexia",
    "Liver Big",
    "Spleen Palpable",
    "Ascites",
    "Spiders",

]


TARGET = "Class"


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 75)
print("       CHRONICCARE AI - PATIENT LIVER MODEL")
print("=" * 75)


df = pd.read_csv(
    DATASET_FILE
)


df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


print(
    f"\nDataset shape: {df.shape}"
)


# ============================================================
# VERIFY COLUMNS
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
# NORMALIZE TARGET
# ============================================================

# ============================================================
# NORMALIZE TARGET
# ============================================================

print("\nRaw target values:")

print(
    df[TARGET]
    .value_counts(dropna=False)
    .to_string()
)


# The UCI Hepatitis dataset documents:
# DIE  = adverse outcome
# LIVE = survival outcome
#
# Depending on how the repository package exports the target,
# values may appear as text or numeric codes.
#
# We support both representations.

raw_target = (
    df[TARGET]
    .astype(str)
    .str.strip()
    .str.upper()
)


target_mapping = {

    "DIE": 1,

    "LIVE": 0,

    "1": 1,

    "2": 0,

}


df[TARGET] = (
    raw_target
    .map(target_mapping)
)


unknown_targets = sorted(
    raw_target[
        df[TARGET].isna()
    ].unique()
)


if unknown_targets:

    raise ValueError(
        "Unknown target values found: "
        + ", ".join(unknown_targets)
    )


df = df.dropna(
    subset=[TARGET]
)


df[TARGET] = (
    df[TARGET]
    .astype(int)
)

# ============================================================
# CLEAN FEATURES
# ============================================================

X = df[PATIENT_FEATURES].copy()

y = df[TARGET].copy()


# Numeric age

X["Age"] = pd.to_numeric(
    X["Age"],
    errors="coerce"
)


# Normalize categorical values

categorical_features = [

    "Sex",
    "Fatigue",
    "Malaise",
    "Anorexia",
    "Liver Big",
    "Spleen Palpable",
    "Ascites",
    "Spiders",

]


for column in categorical_features:

    X[column] = (
        X[column]
        .astype(str)
        .str.strip()
        .str.lower()
    )


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
    y.value_counts()
    .sort_index()
    .to_string()
)


# ============================================================
# PREPROCESSING
# ============================================================

numeric_features = [
    "Age"
]


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
# SPLIT
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
# MODELS
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
# TRAIN
# ============================================================

best_pipeline = None

best_name = None

best_f1 = -1

best_metrics = None


for model_name, model in models.items():

    print(
        "\n" + "-" * 70
    )

    print(
        f"Training: {model_name}"
    )

    print(
        "-" * 70
    )


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

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )


    if f1 > best_f1:

        best_f1 = f1

        best_pipeline = pipeline

        best_name = model_name

        best_metrics = {

            "Accuracy":
                accuracy,

            "Precision":
                precision,

            "Recall":
                recall,

            "F1 Score":
                f1,

        }


# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(
    best_pipeline,
    MODEL_FILE
)


# ============================================================
# REPORT
# ============================================================

report = pd.DataFrame([

    {

        "Disease":
            "liver",

        "Dataset":
            "UCI Hepatitis",

        "Mode":
            "patient",

        "Model":
            best_name,

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
# FINAL
# ============================================================

print(
    "\n" + "=" * 75
)

print(
    "BEST PATIENT LIVER MODEL"
)

print(
    "=" * 75
)

print(
    f"Model     : {best_name}"
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
    f"Model     : {MODEL_FILE}"
)

print(
    f"Report    : {REPORT_FILE}"
)

print(
    "\n✅ PATIENT LIVER MODEL COMPLETE"
)

print("=" * 75)