from django.urls import path

from .views import PredictionView

url_patterns = [path("predict/", PredictionView.as_view(), name="predict")]
