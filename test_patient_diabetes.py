from predictor.ml_predictor import predict_patient_diabetes


sample = {

    "age": 35,

    "gender": "Male",

    "polyuria": "No",

    "polydipsia": "No",

    "sudden_weight_loss": "No",

    "weakness": "No",

    "polyphagia": "No",

    "visual_blurring": "No",

    "obesity": "No",

}


print("=" * 70)
print("   CHRONICCARE AI - PATIENT DIABETES TEST")
print("=" * 70)


try:

    prediction, probability = (
        predict_patient_diabetes(sample)
    )

    print(
        f"\nPrediction : {prediction}"
    )

    if probability is not None:

        print(
            f"Probability: {probability:.2f}%"
        )

    else:

        print(
            "Probability: Not available"
        )

    print("\n✅ PATIENT MODEL SUCCESS")

except Exception as error:

    print("\n❌ PATIENT MODEL FAILED")

    print(error)


print("\n" + "=" * 70)
print("PATIENT DIABETES TEST COMPLETE")