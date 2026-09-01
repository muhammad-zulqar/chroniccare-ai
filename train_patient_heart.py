from predictor.ml_predictor import predict_patient_heart


sample = {

    "age": 45,

    "sex": 1,

    "cp": 1,

    "trestbps": 120,

    "chol": 200,

    "fbs": 0,

    "restecg": 0,

    "thalach": 150,

    "exang": 0,

}


print("=" * 70)
print("   CHRONICCARE AI - PATIENT HEART TEST")
print("=" * 70)


try:

    prediction, probability = (
        predict_patient_heart(sample)
    )

    print(
        f"\nPrediction : {prediction}"
    )

    if probability is not None:

        print(
            f"Probability: {probability:.2f}%"
        )

    print(
        "\n✅ PATIENT HEART MODEL SUCCESS"
    )

except Exception as error:

    print(
        "\n❌ PATIENT HEART MODEL FAILED"
    )

    print(error)


print("\n" + "=" * 70)