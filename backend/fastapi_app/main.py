from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uuid, subprocess, os
import whisper
from gtts import gTTS
from services.llm import get_ai_reply


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")

model = whisper.load_model("base")
def convert_to_wav(input_path, output_path):
    subprocess.run(["ffmpeg", "-y", "-i", input_path, output_path])


@app.post("/voice-chat/")
async def voice_chat(file: UploadFile = File(...)):
    webm_path = f"/tmp/{uuid.uuid4()}.webm"
    wav_path = f"/tmp/{uuid.uuid4()}.wav"

    with open(webm_path, "wb") as f:
        f.write(await file.read())

    convert_to_wav(webm_path, wav_path)

    result = model.transcribe(
        wav_path,
        language="hi",
        task="transcribe"
    )
    user_text = result["text"]

    ai_text = get_ai_reply(user_text)

    # 🔊 English TTS
    tts = gTTS(text=ai_text, lang="hi")
    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_path = os.path.join(AUDIO_DIR, audio_filename)
    tts.save(audio_path)

    return {
        "user_text": user_text,
        "ai_text": ai_text,
        "audio_url": f"http://localhost:8001/audio/{audio_filename}"
    }
