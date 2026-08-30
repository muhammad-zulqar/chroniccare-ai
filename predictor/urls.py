from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "predict/<str:disease>/",
        views.predict,
        name="predict"
    ),
    path(
    "disease/<str:disease>/",
    views.disease_info,
    name="disease_info"
),
path(
    "ai-lab/",
    views.ai_lab,
    name="ai_lab"
),
path(
    "history/",
    views.history,
    name="history"
),
path(
    "about/",
    views.about,
    name="about"
),
]