from django.urls import path
from .views import GenerateTextView, ChatView

urlpatterns = [
    path('generate/', GenerateTextView.as_view(), name='generate_text'),
    path('chat/', ChatView.as_view(), name='chat'),
]