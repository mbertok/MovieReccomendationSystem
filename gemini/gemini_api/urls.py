from django.urls import path

from .views import ChatView, GenerateTextView

urlpatterns = [
    path("generate/", GenerateTextView.as_view(), name="generate_text"),
    path("chat/", ChatView.as_view(), name="chat"),
]
