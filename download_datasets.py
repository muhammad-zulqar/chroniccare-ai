from ucimlrepo import fetch_ucirepo
import pandas as pd
from pathlib import Path

DATASET_DIR = Path("dataset")
DATASET_DIR.mkdir(exist_ok=True)


def save_dataset(uci_id, filename):
    print(f"\nDownloading dataset {uci_id}...")

    dataset = fetch_ucirepo(id=uci_id)

    X = dataset.data.features
    y = dataset.data.targets

    df = pd.concat([X, y], axis=1)

    filepath = DATASET_DIR / filename
    df.to_csv(filepath, index=False)

    print(f"Saved: {filepath}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


# 1. Heart Disease
save_dataset(45, "heart_disease.csv")

# 2. Early Stage Diabetes
save_dataset(529, "diabetes.csv")

# 3. Chronic Kidney Disease
save_dataset(336, "kidney_disease.csv")

# 4. Breast Cancer Wisconsin Diagnostic
save_dataset(17, "breast_cancer.csv")

# 5. Indian Liver Patient Dataset
save_dataset(225, "liver_disease.csv")


print("\n===================================")
print("ALL DATASETS DOWNLOADED SUCCESSFULLY")
print("===================================")