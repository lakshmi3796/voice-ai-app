import { useRef, useState } from "react";

function App() {
  const mediaRecorderRef = useRef(null);
  const [recording, setRecording] = useState(false);
  const [result, setResult] = useState(null);
  const audioRef = useRef(null);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: {
        noiseSuppression: true,
        echoCancellation: true
      }
    });

    const recorder = new MediaRecorder(stream);
    mediaRecorderRef.current = recorder;

    const chunks = [];
    recorder.ondataavailable = (e) => chunks.push(e.data);

    recorder.onstop = async () => {
      const blob = new Blob(chunks, { type: "audio/webm" });

      const formData = new FormData();
      formData.append("file", blob, "voice.webm");

      const res = await fetch("http://localhost:8001/voice-chat/", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      setResult(data);

      // 🔊 Auto-play AI voice
      if (audioRef.current) {
        audioRef.current.src = data.audio_url;
        audioRef.current.play();
      }
    };

    recorder.start();
    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  return (
    <div style={{ padding: 30 }}>
      <h2>🎙️ English Voice AI Tutor</h2>

      {!recording ? (
        <button onClick={startRecording}>Start Speaking</button>
      ) : (
        <button onClick={stopRecording}>Stop</button>
      )}

      {result && (
        <div style={{ marginTop: 20 }}>
          <p><b>You:</b> {result.user_text}</p>
          <p><b>AI:</b> {result.ai_text}</p>
        </div>
      )}

      <audio ref={audioRef} controls style={{ marginTop: 20 }} />
    </div>
  );
}

export default App;
