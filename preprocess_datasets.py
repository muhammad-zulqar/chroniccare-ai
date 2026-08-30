import pandas as pd
from pathlib import Path

DATASET_DIR = Path("dataset")
PROCESSED_DIR = Path("dataset/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_text(value):
    """Remove unwanted whitespace from text values."""
    if isinstance(value, str):
        return value.strip()
    return value


def clean_dataset(filename):
    print("\n" + "=" * 70)
    print(f"PROCESSING: {filename}")
    print("=" * 70)

    input_file = DATASET_DIR / filename

    if not input_file.exists():
        print(f"❌ File not found: {input_file}")
        return

    df = pd.read_csv(input_file)

    print(f"Original shape: {df.shape}")

    # ---------------------------------------------------------
    # 1. Clean column names
    # ---------------------------------------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # ---------------------------------------------------------
    # 2. Remove unwanted whitespace from string values
    # ---------------------------------------------------------
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].apply(clean_text)

    # Convert common missing-value symbols to NaN
    df = df.replace(
        ["?", "NA", "N/A", "na", "null", "None", ""],
        pd.NA
    )

    # ---------------------------------------------------------
    # 3. Remove duplicate rows
    # ---------------------------------------------------------
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        print(f"Removing {duplicate_count} duplicate rows...")
        df = df.drop_duplicates()

    # ---------------------------------------------------------
    # 4. Display missing values
    # ---------------------------------------------------------
    print("\nMissing values before processing:")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values.")
    else:
        print(missing.to_string())

    # ---------------------------------------------------------
    # 5. Convert numeric-looking columns
    # ---------------------------------------------------------
    for column in df.columns:
        if df[column].dtype == "object":
            converted = pd.to_numeric(df[column], errors="coerce")

            # Convert only when most values can be numeric
            valid_ratio = converted.notna().mean()

            if valid_ratio > 0.8:
                df[column] = converted

    # ---------------------------------------------------------
    # 6. Fill missing numerical values with median
    # ---------------------------------------------------------
    numerical_columns = df.select_dtypes(
        include=["int64", "float64", "Int64", "Float64"]
    ).columns

    for column in numerical_columns:
        if df[column].isnull().any():
            df[column] = df[column].fillna(df[column].median())

    # ---------------------------------------------------------
    # 7. Fill missing categorical values with mode
    # ---------------------------------------------------------
    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:
        if df[column].isnull().any():

            mode = df[column].mode()

            if not mode.empty:
                df[column] = df[column].fillna(mode[0])

    # ---------------------------------------------------------
    # 8. Save cleaned dataset
    # ---------------------------------------------------------
    output_file = PROCESSED_DIR / filename

    df.to_csv(output_file, index=False)

    print(f"\nFinal shape: {df.shape}")
    print(f"Saved to: {output_file}")
    print("✅ Processing completed.")


# -------------------------------------------------------------
# DATASETS
# -------------------------------------------------------------

datasets = [
    "heart_disease.csv",
    "diabetes.csv",
    "kidney_disease.csv",
    "breast_cancer.csv",
    "liver_disease.csv",
]


for dataset in datasets:
    clean_dataset(dataset)


print("\n" + "=" * 70)
print("ALL DATASETS PROCESSED")
print("=" * 70)