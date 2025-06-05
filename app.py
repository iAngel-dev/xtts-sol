import gradio as gr
import time

def speak(text):
    return "https://upload.wikimedia.org/wikipedia/commons/4/45/Example.ogg"

iface = gr.Interface(fn=speak, 
                     inputs=gr.Textbox(lines=2, placeholder="Écris ici pour que Sol parle..."),
                     outputs="audio",
                     title="Sol vocal",
                     description="Assistant vocal XTTS")

iface.launch(server_port=8020, server_name="0.0.0.0")
