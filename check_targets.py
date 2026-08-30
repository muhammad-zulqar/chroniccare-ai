import pandas as pd
from pathlib import Path

DATASET_DIR = Path("dataset")

print("=" * 70)
print("        CHRONICCARE AI - TARGET COLUMN CHECK")
print("=" * 70)

for file in DATASET_DIR.glob("*.csv"):

    print("\n" + "=" * 70)
    print(f"FILE: {file.name}")
    print("=" * 70)

    df = pd.read_csv(file)

    print("\nColumns:")
    for i, column in enumerate(df.columns, start=1):
        print(f"{i}. {column}")

    print("\nLast column:")
    print(df.columns[-1])

    print("\nLast column values:")
    print(df.iloc[:, -1].value_counts(dropna=False).to_string())

print("\n" + "=" * 70)
print("CHECK COMPLETE")
print("=" * 70)