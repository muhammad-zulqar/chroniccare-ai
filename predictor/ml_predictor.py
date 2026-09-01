from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "ml_models"


MODEL_PATHS = {
    "heart_disease": MODEL_DIR / "heart_disease_model.joblib",
    "diabetes": MODEL_DIR / "diabetes_model.joblib",
    "kidney_disease": MODEL_DIR / "kidney_disease_model.joblib",
    "breast_cancer": MODEL_DIR / "breast_cancer_model.joblib",
    "liver_disease": MODEL_DIR / "liver_disease_model.joblib",
    "diabetes_patient": MODEL_DIR / "diabetes_patient_model.joblib",
    "heart_patient":MODEL_DIR / "heart_disease_patient_model.joblib",
    "kidney_patient":MODEL_DIR / "kidney_disease_patient_model.joblib",
    "liver_patient":MODEL_DIR / "liver_patient_model.joblib",
}

PATIENT_KIDNEY_FEATURES = [

    "age",
    "bp",
    "bgr",
    "bu",
    "sc",
    "hemo",
    "htn",
    "dm",
    "appet",
    "pe",

]

PATIENT_HEART_FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
]

PATIENT_DIABETES_FEATURES = [
    "age",
    "gender",
    "polyuria",
    "polydipsia",
    "sudden_weight_loss",
    "weakness",
    "polyphagia",
    "visual_blurring",
    "obesity",
]
PATIENT_LIVER_FEATURES = [
    "Age",
    "Sex",
    "Fatigue",
    "Malaise",
    "Anorexia",
    "Liver Big",
    "Spleen Palpable",
    "Ascites",
    "Spiders",
]
# Numeric fields for each model
NUMERIC_FIELDS = {

    

    "heart_disease": {
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal",
    },

    

    "diabetes": {
        "age",
    },

    "kidney_disease": {
        "age",
        "bp",
        "sg",
        "al",
        "su",
        "bgr",
        "bu",
        "sc",
        "sod",
        "pot",
        "hemo",
        "pcv",
        "wbcc",
        "rbcc",
    },

    "breast_cancer": {
        "radius1",
        "texture1",
        "perimeter1",
        "area1",
        "smoothness1",
        "compactness1",
        "concavity1",
        "concave_points1",
        "symmetry1",
        "fractal_dimension1",
        "radius2",
        "texture2",
        "perimeter2",
        "area2",
        "smoothness2",
        "compactness2",
        "concavity2",
        "concave_points2",
        "symmetry2",
        "fractal_dimension2",
        "radius3",
        "texture3",
        "perimeter3",
        "area3",
        "smoothness3",
        "compactness3",
        "concavity3",
        "concave_points3",
        "symmetry3",
        "fractal_dimension3",
    },

    "liver_disease": {
        "age",
        "tb",
        "db",
        "alkphos",
        "sgpt",
        "sgot",
        "tp",
        "alb",
        "a/g_ratio",
    },
}

def predict_patient_diabetes(data):

    model = joblib.load(
        MODEL_PATHS["diabetes_patient"]
    )

    input_data = pd.DataFrame(
        [data],
        columns=PATIENT_DIABETES_FEATURES
    )

    prediction = model.predict(
        input_data
    )[0]

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        classes = list(
            model.classes_
        )

        if 1 in classes:

            positive_index = classes.index(1)

            probability = float(
                probabilities[positive_index] * 100
            )

    return int(prediction), probability
def load_model(disease):

    model_path = MODEL_PATHS.get(disease)

    if model_path is None:
        raise ValueError(
            f"Unknown disease: {disease}"
        )

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    return joblib.load(model_path)


def prepare_input(disease, data):

    cleaned_data = {}

    numeric_fields = NUMERIC_FIELDS.get(
        disease,
        set()
    )

    for field, value in data.items():

        if field in numeric_fields:

            try:
                cleaned_data[field] = float(value)

            except (ValueError, TypeError):

                raise ValueError(
                    f"Invalid numeric value for: {field}"
                )

        else:

            cleaned_data[field] = str(value).strip()

    return pd.DataFrame([cleaned_data])


def predict_disease(disease, data):

    model = load_model(disease)

    input_data = prepare_input(
        disease,
        data
    )

    prediction = model.predict(
        input_data
    )[0]

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        probability = float(
            probabilities[1] * 100
        )

    return prediction, probability

def predict_patient_heart(data):

    model = joblib.load(
        MODEL_PATHS["heart_patient"]
    )

    input_data = pd.DataFrame(
        [data],
        columns=PATIENT_HEART_FEATURES
    )

    prediction = model.predict(
        input_data
    )[0]

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        classes = list(
            model.classes_
        )

        if 1 in classes:

            positive_index = classes.index(1)

            probability = float(
                probabilities[positive_index] * 100
            )

    return int(prediction), probability

def predict_patient_kidney(data):

    model = joblib.load(
        MODEL_PATHS["kidney_patient"]
    )

    input_data = pd.DataFrame(
        [data],
        columns=PATIENT_KIDNEY_FEATURES
    )

    prediction = model.predict(
        input_data
    )[0]

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        classes = list(
            model.classes_
        )

        if 1 in classes:

            positive_index = classes.index(1)

            probability = float(
                probabilities[positive_index] * 100
            )

    return int(prediction), probability

def predict_patient_liver(data):

    model = joblib.load(
        MODEL_PATHS["liver_patient"]
    )

    input_data = pd.DataFrame(
        [data],
        columns=PATIENT_LIVER_FEATURES
    )

    prediction = model.predict(
        input_data
    )[0]

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        classes = list(
            model.classes_
        )

        if 1 in classes:

            positive_index = classes.index(1)

            probability = float(
                probabilities[positive_index] * 100
            )

    return int(prediction), probability