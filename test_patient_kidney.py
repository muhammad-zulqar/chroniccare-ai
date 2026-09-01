from predictor.ml_predictor import predict_patient_kidney


sample = {

    "age": 45,

    "bp": 80,

    "bgr": 120,

    "bu": 40,

    "sc": 1.2,

    "hemo": 13.5,

    "htn": "no",

    "dm": "no",

    "appet": "good",

    "pe": "no",

}


print("=" * 70)
print("   CHRONICCARE AI - PATIENT KIDNEY TEST")
print("=" * 70)


try:

    prediction, probability = (
        predict_patient_kidney(sample)
    )

    print(
        f"\nPrediction : {prediction}"
    )

    if probability is not None:

        print(
            f"Probability: {probability:.2f}%"
        )

    print(
        "\n✅ PATIENT KIDNEY MODEL SUCCESS"
    )

except Exception as error:

    print(
        "\n❌ PATIENT KIDNEY MODEL FAILED"
    )

    print(error)


print("\n" + "=" * 70)