import pandas as pd
from pathlib import Path

DATASET_DIR = Path("dataset")

print("=" * 70)
print("           CHRONICCARE AI - DATASET INSPECTION")
print("=" * 70)

csv_files = list(DATASET_DIR.glob("*.csv"))

if not csv_files:
    print("\n❌ No CSV files found inside the dataset folder.")
    exit()

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"DATASET: {file.name}")
    print("=" * 70)

    try:
        df = pd.read_csv(file)

        # Basic information
        print(f"\nRows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\n--- COLUMN NAMES ---")
        for column in df.columns:
            print(f"  • {column}")

        # Data types
        print("\n--- DATA TYPES ---")
        print(df.dtypes)

        # Missing values
        print("\n--- MISSING VALUES ---")
        missing = df.isnull().sum()

        missing_found = False

        for column, count in missing.items():
            if count > 0:
                print(f"  • {column}: {count}")
                missing_found = True

        if not missing_found:
            print("  No missing values found.")

        # Duplicate records
        print("\n--- DUPLICATE RECORDS ---")
        duplicates = df.duplicated().sum()
        print(f"  {duplicates}")

        # First 5 rows
        print("\n--- FIRST 5 ROWS ---")
        print(df.head().to_string())

        # Numerical columns
        print("\n--- NUMERICAL COLUMNS ---")
        numerical = df.select_dtypes(include="number").columns.tolist()

        if numerical:
            print(", ".join(numerical))
        else:
            print("No numerical columns.")

        # Categorical columns
        print("\n--- CATEGORICAL COLUMNS ---")
        categorical = df.select_dtypes(exclude="number").columns.tolist()

        if categorical:
            print(", ".join(categorical))
        else:
            print("No categorical columns.")

        # Statistical summary
        print("\n--- STATISTICAL SUMMARY ---")

        if numerical:
            print(df[numerical].describe().round(2).to_string())

        print("\n✅ Dataset inspection completed.")

    except Exception as e:
        print(f"\n❌ ERROR reading {file.name}")
        print(e)


print("\n" + "=" * 70)
print("             INSPECTION FINISHED")
print("=" * 70)