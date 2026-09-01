from django.shortcuts import render
from .models import Prediction
from .ml_predictor import (
    predict_disease,
    predict_patient_diabetes,
    predict_patient_heart,
    predict_patient_kidney,
    predict_patient_liver,
)
from .forms_config import DISEASE_FORMS
from django.contrib.auth.decorators import login_required
import pandas as pd
from pathlib import Path
from .screening import screen_breast_health


def home(request):
    return render(
        request,
        "predictor/home.html"
    )
def ai_lab(request):

    reports_dir = (
        Path(__file__).resolve().parent.parent
        / "documentation"
        / "ml_reports"
    )

    performance_file = (
        reports_dir / "model_performance.csv"
    )

    performance = []

    if performance_file.exists():

        df = pd.read_csv(
            performance_file
        )

        for _, row in df.iterrows():

            performance.append({
                "Disease": row["Disease"],
                "Accuracy": f"{row['Accuracy']:.4f}",
                "Precision": f"{row['Precision']:.4f}",
                "Recall": f"{row['Recall']:.4f}",
                "F1_Score": f"{row['F1 Score']:.4f}",
                "Model": "Selected ML Model",
            })

    return render(
        request,
        "predictor/ai_lab.html",
        {
            "performance": performance,
            "reports": [],
        }
    )
@login_required(login_url="login")
def dashboard(request):

    return render(
        request,
        "predictor/dashboard.html"
    )
def about(request):

    return render(
        request,
        "predictor/about.html"
    )
@login_required(login_url="login")
def history(request):

    predictions = Prediction.objects.filter(
        user=request.user
    ).order_by("-created_at")

    total = predictions.count()

    positive = predictions.filter(
        prediction=1
    ).count()

    negative = predictions.filter(
        prediction=0
    ).count()

    return render(
        request,
        "predictor/history.html",
        {
            "predictions": predictions,
            "total": total,
            "positive": positive,
            "negative": negative,
        }
    )
def disease_info(request, disease):

    form_config = DISEASE_FORMS.get(disease)

    if not form_config:

        return render(
            request,
            "predictor/disease_info.html",
            {
                "error": "Disease information not found."
            }
        )

    return render(
        request,
        "predictor/disease_info.html",
        {
            "disease": disease,
            "title": form_config["title"],
            "description": form_config["description"],
            "fields": form_config["fields"],
        }
    )

def get_risk_level(probability):

    if probability is None:
        return "Unavailable"

    if probability < 30:
        return "Lower"

    elif probability < 70:
        return "Moderate"

    return "Higher"

@login_required(login_url="login")
def predict(request, disease):

    form_config = DISEASE_FORMS.get(disease)

    if not form_config:

        return render(
            request,
            "predictor/predict.html",
            {
                "error": "Disease assessment not found."
            }
        )

    result = None
    probability = None
    risk_level = None
    error = None

    fields = form_config["fields"]

    if request.method == "POST":

        try:

            data = {}

            for field in fields:

                field_name = field["name"]

                value = request.POST.get(
                    field_name
                )

                if value is None or value == "":

                    raise ValueError(
                        f"Please complete: {field['label']}"
                    )

                data[field_name] = value

            if disease == "diabetes":
                result, probability = predict_patient_diabetes(data)
            elif disease == "heart_disease":
                result, probability = predict_patient_heart(data)
            elif disease == "kidney_disease":
                result, probability = predict_patient_kidney(data)
            elif disease == "liver_disease":
                result, probability = predict_patient_liver(data)
            elif disease == "breast_cancer":
                screening = screen_breast_health(data)
                return render(
                    request,
                    "predictor/breast_screening_result.html",
                    {
                        "screening": screening,
                        "disease": disease,
                        "title": form_config["title"],
                    }
                )
            else:
                result, probability = predict_disease(disease, data)

            risk_level = get_risk_level(probability)

            Prediction.objects.create(
                user=request.user if request.user.is_authenticated else None,
                disease=disease,
                risk_level=risk_level,
                probability=probability if probability is not None else 0,
                prediction=int(result),
            )

            return render(
                request,
                "predictor/result.html",
                {
                    "disease": disease,
                    "result": int(result),
                    "probability": probability,
                    "risk_level": risk_level,
                }
            )

        except Exception as e:

            error = str(e)

    return render(
        request,
        "predictor/predict.html",
        {
            "disease": disease,
            "title": form_config["title"],
            "description": form_config["description"],
            "fields": fields,
            "error": error,
        }
    )