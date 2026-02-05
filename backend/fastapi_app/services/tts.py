
from gtts import gTTS
import uuid, os

os.makedirs("temp", exist_ok=True)

def text_to_speech(text: str) -> str:
    filename = f"temp/{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename
