import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)


# ============================================================
# PATHS
# ============================================================

DATASET_DIR = Path("dataset/processed")
MODEL_DIR = Path("ml_models")


# ============================================================
# DATASET CONFIGURATION
# ============================================================

DATASETS = {
    "heart_disease": {
        "file": "heart_disease.csv",
        "target": "num"
    },

    "diabetes": {
        "file": "diabetes.csv",
        "target": "class"
    },

    "kidney_disease": {
        "file": "kidney_disease.csv",
        "target": "class"
    },

    "breast_cancer": {
        "file": "breast_cancer.csv",
        "target": "diagnosis"
    },

    "liver_disease": {
        "file": "liver_disease.csv",
        "target": "selector"
    }
}


# ============================================================
# TARGET CONVERSION
# ============================================================

def convert_target(name, y):

    y = y.astype(str).str.strip()

    if name == "heart_disease":

        return y.apply(
            lambda value: 0 if value == "0" else 1
        )

    if name == "diabetes":

        return y.map({
            "Negative": 0,
            "Positive": 1
        })

    if name == "kidney_disease":

        return y.map({
            "notckd": 0,
            "ckd": 1
        })

    if name == "breast_cancer":

        return y.map({
            "B": 0,
            "M": 1
        })

    if name == "liver_disease":

        return y.map({
            "1": 1,
            "2": 0
        })


# ============================================================
# EVALUATE
# ============================================================

for disease, config in DATASETS.items():

    print("\n")
    print("=" * 75)
    print(f"        {disease.upper()}")
    print("=" * 75)

    dataset_path = DATASET_DIR / config["file"]
    model_path = MODEL_DIR / f"{disease}_model.joblib"

    df = pd.read_csv(dataset_path)

    X = df.drop(columns=[config["target"]])

    y = convert_target(
        disease,
        df[config["target"]]
    )

    valid = y.notna()

    X = X.loc[valid]
    y = y.loc[valid].astype(int)

    # Same test split used during training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Load trained pipeline
    model = joblib.load(model_path)

    predictions = model.predict(X_test)

    print("\n📊 PERFORMANCE")

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

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    # --------------------------------------------------------
    # ROC AUC
    # --------------------------------------------------------

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(X_test)[:, 1]

        auc = roc_auc_score(
            y_test,
            probabilities
        )

        print(f"ROC-AUC  : {auc:.4f}")

    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    print("\n🔲 CONFUSION MATRIX")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    # --------------------------------------------------------
    # CLASSIFICATION REPORT
    # --------------------------------------------------------

    print("\n📋 CLASSIFICATION REPORT")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )


print("\n")
print("=" * 75)
print("        CHRONICCARE AI - EVALUATION COMPLETE")
print("=" * 75)