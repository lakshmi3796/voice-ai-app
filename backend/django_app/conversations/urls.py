# conversations/urls.py
from django.urls import path
from .views import VoiceChatView

urlpatterns = [
    path("voice-chat/", VoiceChatView.as_view()),
]
