import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Conversation

class VoiceChatView(APIView):
    def post(self, request):
        audio = request.FILES["audio"]
        target_language = request.POST.get("target_language", "English")

        resp = requests.post(
            "http://localhost:8001/voice-chat/",
            files={"audio": audio},
            data={"target_language": target_language}
        )

        data = resp.json()
        Conversation.objects.create(
            user_text=data["user_text"],
            ai_text=data["ai_text"]
        )
        return Response(data)
