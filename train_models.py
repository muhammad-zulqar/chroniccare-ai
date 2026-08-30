import pandas as pd
import numpy as np
from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from sklearn.base import clone


# ============================================================
# PATHS
# ============================================================

DATASET_DIR = Path("dataset/processed")
MODEL_DIR = Path("ml_models")

MODEL_DIR.mkdir(exist_ok=True)


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

        # 0 = no disease
        # 1,2,3,4 = disease

        return y.apply(
            lambda value: 0 if value == "0" else 1
        )

    elif name == "diabetes":

        mapping = {
            "Negative": 0,
            "Positive": 1
        }

        return y.map(mapping)

    elif name == "kidney_disease":

        mapping = {
            "notckd": 0,
            "ckd": 1
        }

        return y.map(mapping)

    elif name == "breast_cancer":

        mapping = {
            "B": 0,
            "M": 1
        }

        return y.map(mapping)

    elif name == "liver_disease":

        # UCI ILPD:
        # 1 = liver disease
        # 2 = no liver disease

        return y.map({
            "1": 1,
            "2": 0
        })

    return y


# ============================================================
# MODELS
# ============================================================

MODELS = {

    "Logistic Regression": LogisticRegression(
        max_iter=2000
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )
}


# ============================================================
# TRAIN FUNCTION
# ============================================================

def train_disease_model(name, config):

    print("\n")
    print("=" * 75)
    print(f"TRAINING: {name.upper()}")
    print("=" * 75)

    file_path = DATASET_DIR / config["file"]
    target_column = config["target"]

    if not file_path.exists():
        print(f"❌ Dataset not found: {file_path}")
        return None

    df = pd.read_csv(file_path)

    print(f"Dataset shape: {df.shape}")

    # --------------------------------------------------------
    # Separate features and target
    # --------------------------------------------------------

    X = df.drop(columns=[target_column])

    y = convert_target(
        name,
        df[target_column]
    )

    valid_rows = y.notna()

    X = X.loc[valid_rows].copy()
    y = y.loc[valid_rows].astype(int)

    print("\nTarget distribution:")
    print(y.value_counts().to_string())

    # --------------------------------------------------------
    # Detect feature types
    # --------------------------------------------------------

    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    print("\nNumerical features:")
    print(numerical_features)

    print("\nCategorical features:")
    print(categorical_features)

    # --------------------------------------------------------
    # Preprocessing
    # --------------------------------------------------------

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore")
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numerical_pipeline,
                numerical_features
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features
            )
        ]
    )

    # --------------------------------------------------------
    # Train/Test split
    # --------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # --------------------------------------------------------
    # Track best model
    # --------------------------------------------------------

    best_model = None
    best_name = None
    best_f1 = -1

    best_metrics = {
        "Accuracy": 0,
        "Precision": 0,
        "Recall": 0,
        "F1 Score": 0,
    }

    # --------------------------------------------------------
    # Train candidate models
    # --------------------------------------------------------

    for model_name, model in MODELS.items():

        print("\n" + "-" * 60)
        print(f"Model: {model_name}")
        print("-" * 60)

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    clone(preprocessor)
                ),
                (
                    "model",
                    clone(model)
                )
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

        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")

        print("\nConfusion Matrix:")

        print(
            confusion_matrix(
                y_test,
                predictions
            )
        )

        if f1 > best_f1:

            best_f1 = f1
            best_model = pipeline
            best_name = model_name

            best_metrics = {
                "Accuracy": accuracy,
                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1,
            }

    # --------------------------------------------------------
    # Save best model
    # --------------------------------------------------------

    model_path = MODEL_DIR / f"{name}_model.joblib"

    joblib.dump(
        best_model,
        model_path
    )

    print("\n" + "=" * 75)
    print("BEST MODEL")
    print("=" * 75)

    print(f"Model      : {best_name}")
    print(f"Accuracy   : {best_metrics['Accuracy']:.4f}")
    print(f"Precision  : {best_metrics['Precision']:.4f}")
    print(f"Recall     : {best_metrics['Recall']:.4f}")
    print(f"F1 Score   : {best_metrics['F1 Score']:.4f}")
    print(f"Saved      : {model_path}")

    print("\n✅ Training completed.")

    # Return information for report generation
    return {
        "Disease": name,
        "Model": best_name,
        "Accuracy": best_metrics["Accuracy"],
        "Precision": best_metrics["Precision"],
        "Recall": best_metrics["Recall"],
        "F1 Score": best_metrics["F1 Score"],
        "Features": X.shape[1],
        "Training Samples": len(X_train),
        "Testing Samples": len(X_test),
    }