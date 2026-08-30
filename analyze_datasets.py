import pandas as pd
from pathlib import Path

DATASET_DIR = Path("dataset/processed")

print("=" * 80)
print("             CHRONICCARE AI - DATASET ANALYSIS")
print("=" * 80)

for file in DATASET_DIR.glob("*.csv"):

    print("\n" + "=" * 80)
    print(f"DATASET: {file.name}")
    print("=" * 80)

    df = pd.read_csv(file)

    # ---------------------------------------------------------
    # BASIC INFORMATION
    # ---------------------------------------------------------

    print("\n📊 BASIC INFORMATION")
    print("-" * 40)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # ---------------------------------------------------------
    # COLUMNS
    # ---------------------------------------------------------

    print("\n📋 COLUMNS")
    print("-" * 40)

    for column in df.columns:
        print(f"• {column}")

    # ---------------------------------------------------------
    # DATA TYPES
    # ---------------------------------------------------------

    print("\n🔤 DATA TYPES")
    print("-" * 40)

    print(df.dtypes.to_string())

    # ---------------------------------------------------------
    # MISSING VALUES
    # ---------------------------------------------------------

    print("\n❓ MISSING VALUES")
    print("-" * 40)

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("No missing values.")
    else:
        print(missing[missing > 0].to_string())

    # ---------------------------------------------------------
    # DUPLICATES
    # ---------------------------------------------------------

    print("\n♻️ DUPLICATES")
    print("-" * 40)

    print(f"Duplicate rows: {df.duplicated().sum()}")

    # ---------------------------------------------------------
    # NUMERICAL SUMMARY
    # ---------------------------------------------------------

    print("\n📈 NUMERICAL SUMMARY")
    print("-" * 40)

    numerical = df.select_dtypes(include="number")

    if not numerical.empty:
        print(
            numerical.describe()
            .round(2)
            .to_string()
        )
    else:
        print("No numerical columns.")

    # ---------------------------------------------------------
    # CATEGORICAL VALUES
    # ---------------------------------------------------------

    print("\n🔤 CATEGORICAL VALUES")
    print("-" * 40)

    categorical = df.select_dtypes(include="object")

    if categorical.empty:
        print("No categorical columns.")

    else:
        for column in categorical.columns:

            print(f"\n{column}:")

            values = df[column].value_counts()

            for value, count in values.items():
                print(f"  {value}: {count}")

    # ---------------------------------------------------------
    # TARGET DISTRIBUTION
    # ---------------------------------------------------------

    target = df.columns[-1]

    print("\n🎯 TARGET COLUMN")
    print("-" * 40)

    print(f"Target: {target}")

    print("\nTarget distribution:")

    print(
        df[target]
        .value_counts()
        .to_string()
    )

    # ---------------------------------------------------------
    # FIRST FIVE ROWS
    # ---------------------------------------------------------

    print("\n👀 FIRST FIVE ROWS")
    print("-" * 40)

    print(df.head().to_string())

print("\n" + "=" * 80)
print("                 ANALYSIS COMPLETE")
print("=" * 80)