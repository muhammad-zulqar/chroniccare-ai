from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "dataset"

DATASET_DIR.mkdir(
    parents=True,
    exist_ok=True
)


print("=" * 70)
print("   CHRONICCARE AI - DOWNLOAD LIVER PATIENT DATASET")
print("=" * 70)


print("\nDownloading UCI Hepatitis dataset...")


hepatitis = fetch_ucirepo(
    id=46
)


X = hepatitis.data.features.copy()

y = hepatitis.data.targets.copy()


df = pd.concat(
    [X, y],
    axis=1
)


print(
    f"\nDownloaded shape: {df.shape}"
)


print("\nColumns:")

for number, column in enumerate(
    df.columns,
    start=1
):

    print(
        f"{number:02d}. {column}"
    )


output_file = (
    DATASET_DIR
    / "liver_patient_symptoms.csv"
)


df.to_csv(
    output_file,
    index=False
)


print(
    f"\nSaved to: {output_file}"
)


print("\n✅ DOWNLOAD COMPLETE")

print("=" * 70)