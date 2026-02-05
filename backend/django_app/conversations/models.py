# conversations/models.py
from django.db import models

class Conversation(models.Model):
    user_text = models.TextField()
    ai_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
