import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# PATHS
# ============================================================

DATASET_DIR = Path("dataset/processed")
MODEL_DIR = Path("ml_models")

REPORT_DIR = Path("documentation/ml_reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# DATASETS
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

    elif name == "diabetes":

        return y.map({
            "Negative": 0,
            "Positive": 1
        })

    elif name == "kidney_disease":

        return y.map({
            "notckd": 0,
            "ckd": 1
        })

    elif name == "breast_cancer":

        return y.map({
            "B": 0,
            "M": 1
        })

    elif name == "liver_disease":

        return y.map({
            "1": 1,
            "2": 0
        })


# ============================================================
# PROCESS EACH DISEASE
# ============================================================

results = []


for disease, config in DATASETS.items():

    print(f"\nGenerating reports for {disease}...")

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

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = joblib.load(model_path)

    predictions = model.predict(X_test)

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

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

    results.append({
        "Disease": disease,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    cm = confusion_matrix(
        y_test,
        predictions
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=[
            "No Disease",
            "Disease"
        ]
    )

    display.plot()

    plt.title(
        f"{disease.replace('_', ' ').title()} - Confusion Matrix"
    )

    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / f"{disease}_confusion_matrix.png",
        dpi=200
    )

    plt.close()

    # --------------------------------------------------------
    # ROC CURVE
    # --------------------------------------------------------

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            X_test
        )[:, 1]

        fpr, tpr, _ = roc_curve(
            y_test,
            probabilities
        )

        roc_auc = auc(
            fpr,
            tpr
        )

        plt.figure()

        plt.plot(
            fpr,
            tpr,
            label=f"ROC-AUC = {roc_auc:.3f}"
        )

        plt.plot(
            [0, 1],
            [0, 1],
            linestyle="--"
        )

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")

        plt.title(
            f"{disease.replace('_', ' ').title()} - ROC Curve"
        )

        plt.legend()

        plt.tight_layout()

        plt.savefig(
            REPORT_DIR / f"{disease}_roc_curve.png",
            dpi=200
        )

        plt.close()


# ============================================================
# MODEL COMPARISON
# ============================================================

results_df = pd.DataFrame(results)

print("\n")
print("=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)

print(
    results_df.round(4).to_string(index=False)
)


# ------------------------------------------------------------
# Save CSV
# ------------------------------------------------------------

results_df.to_csv(
    REPORT_DIR / "model_performance.csv",
    index=False
)


# ------------------------------------------------------------
# Create comparison chart
# ------------------------------------------------------------

plot_df = results_df.set_index("Disease")

plot_df[
    [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
].plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title(
    "ChronicCare AI - Model Performance Comparison"
)

plt.ylabel("Score")

plt.ylim(0, 1)

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    REPORT_DIR / "model_performance_comparison.png",
    dpi=200
)

plt.close()


print("\n")
print("=" * 70)
print("REPORT GENERATION COMPLETE")
print("=" * 70)

print(f"\nReports saved in:")
print(REPORT_DIR)