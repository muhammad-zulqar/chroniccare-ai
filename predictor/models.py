from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):

    DISEASE_CHOICES = [
        ("heart_disease", "Heart Disease"),
        ("diabetes", "Diabetes"),
        ("kidney_disease", "Chronic Kidney Disease"),
        ("breast_cancer", "Breast Cancer"),
        ("liver_disease", "Liver Disease"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    disease = models.CharField(
        max_length=50,
        choices=DISEASE_CHOICES
    )

    risk_level = models.CharField(
        max_length=20
    )

    probability = models.FloatField()

    prediction = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.disease} - {self.risk_level}"