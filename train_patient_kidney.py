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
    / "kidney_disease.csv"
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
    / "kidney_disease_patient_model.joblib"
)


# ============================================================
# PATIENT-FRIENDLY FEATURES
# ============================================================

PATIENT_FEATURES = [

    "age",
    "bp",
    "bgr",
    "bu",
    "sc",
    "hemo",
    "htn",
    "dm",
    "appet",
    "pe",

]

TARGET = "class"


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 75)
print("      CHRONICCARE AI - PATIENT KIDNEY MODEL")
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
# CHECK COLUMNS
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

text_features = [

    "htn",
    "dm",
    "appet",
    "pe",

]


for column in text_features:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.lower()
    )


# ============================================================
# CLEAN NUMERICAL FEATURES
# ============================================================

numeric_features = [

    "age",
    "bp",
    "bgr",
    "bu",
    "sc",
    "hemo",

]


for column in numeric_features:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# TARGET
# ============================================================

df[TARGET] = (
    df[TARGET]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(
        r"\s+",
        "",
        regex=True
    )
)


target_mapping = {

    "ckd": 1,

    "notckd": 0,

}


df[TARGET] = (
    df[TARGET]
    .map(target_mapping)
)


# Remove rows where target cannot be understood

df = df.dropna(
    subset=[TARGET]
)


df[TARGET] = (
    df[TARGET]
    .astype(int)
)


# ============================================================
# FEATURES + TARGET
# ============================================================

X = df[PATIENT_FEATURES].copy()

y = df[TARGET].copy()


print(
    f"\nPatient-friendly features: {len(PATIENT_FEATURES)}"
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
    y.value_counts().to_string()
)


# ============================================================
# PIPELINES
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
            text_features
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
# TRAIN MODELS
# ============================================================

best_pipeline = None

best_model_name = None

best_f1 = -1

best_metrics = None


for model_name, model in models.items():

    print("\n" + "-" * 70)

    print(
        f"Training: {model_name}"
    )

    print("-" * 70)


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

        best_model_name = model_name

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
# SAVE REPORT
# ============================================================

report = pd.DataFrame([

    {

        "Disease":
            "kidney_disease",

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
    / "kidney_patient_performance.csv"
)


report.to_csv(
    report_file,
    index=False
)


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 75)

print("BEST PATIENT KIDNEY MODEL")

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
    f"Model     : {MODEL_FILE}"
)

print(
    f"Report    : {report_file}"
)

print(
    "\n✅ PATIENT KIDNEY MODEL COMPLETE"
)

print("=" * 75)