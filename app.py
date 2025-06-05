import gradio as gr
import tempfile
import os

def speak(text):
    # Simule un fichier audio temporaire silencieux (placeholder XTTS)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_audio.write(b"\0" * 10000)
    temp_audio.close()
    return temp_audio.name

iface = gr.Interface(fn=speak,
                     inputs=gr.Textbox(lines=2, placeholder="Écris ici pour que Sol parle..."),
                     outputs="audio",
                     title="Sol vocal",
                     description="Assistant vocal XTTS")

iface.launch(server_port=8020, server_name="0.0.0.0")
