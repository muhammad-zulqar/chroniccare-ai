from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "disease",
        "risk_level",
        "probability",
        "created_at",
    )

    list_filter = (
        "disease",
        "risk_level",
        "created_at",
    )

    search_fields = (
        "user__username",
        "disease",
    )