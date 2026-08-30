from pathlib import Path
import joblib

MODEL_DIR = Path("ml_models")

MODELS = [
    "heart_disease_model.joblib",
    "diabetes_model.joblib",
    "kidney_disease_model.joblib",
    "breast_cancer_model.joblib",
    "liver_disease_model.joblib",
]

print("=" * 70)
print("        CHRONICCARE AI - MODEL VERIFICATION")
print("=" * 70)

all_good = True

for filename in MODELS:

    path = MODEL_DIR / filename

    print(f"\nChecking: {filename}")

    if not path.exists():
        print("❌ FILE NOT FOUND")
        all_good = False
        continue

    try:

        model = joblib.load(path)

        print("✅ Loaded successfully")
        print(f"Type: {type(model).__name__}")

        if hasattr(model, "predict_proba"):
            print("✅ Probability supported")
        else:
            print("⚠️ Probability not supported")

    except Exception as error:

        print("❌ Failed to load")
        print(error)
        all_good = False


print("\n" + "=" * 70)

if all_good:
    print("✅ ALL MODELS ARE READY")
else:
    print("❌ ONE OR MORE MODELS NEED ATTENTION")

print("=" * 70)