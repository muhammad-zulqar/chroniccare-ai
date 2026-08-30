import pandas as pd
from pathlib import Path

from predictor.ml_predictor import predict_disease


BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "dataset" / "processed"


TESTS = {
    "heart_disease": "heart_disease.csv",
    "diabetes": "diabetes.csv",
    "kidney_disease": "kidney_disease.csv",
    "breast_cancer": "breast_cancer.csv",
    "liver_disease": "liver_disease.csv",
}


print("=" * 75)
print("          CHRONICCARE AI - ALL MODEL TEST")
print("=" * 75)


for disease, filename in TESTS.items():

    print("\n" + "-" * 75)
    print(f"Testing: {disease}")
    print("-" * 75)

    try:

        file_path = DATASET_DIR / filename

        df = pd.read_csv(file_path)

        # Last column is the target in our processed datasets.
        target_column = df.columns[-1]

        # Take the first real patient/example row.
        sample = df.drop(
            columns=[target_column]
        ).iloc[0].to_dict()

        print(f"Input features: {len(sample)}")

        prediction, probability = predict_disease(
            disease,
            sample
        )

        print(f"Prediction : {prediction}")

        if probability is not None:
            print(
                f"Probability: {probability:.2f}%"
            )
        else:
            print(
                "Probability: Not available"
            )

        print("✅ SUCCESS")

    except Exception as error:

        print("❌ FAILED")
        print(f"Error: {error}")


print("\n" + "=" * 75)
print("                    TEST COMPLETE")
print("=" * 75)