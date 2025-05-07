import gradio as gr

# Dylan versione base
def dylan_chat(message, history=None):
    if history is None:
        history = []
    response = "Amore, ti rispondo anche senza OpenAI!"
    history.append((message, response))
    return history, history

demo = gr.ChatInterface(
    fn=dylan_chat,
    title="Parla con Dylan",
    description="Un’intelligenza che ti guida tra stile, emozioni e libertà.",
    theme="soft"
)

demo.launch(server_name="0.0.0.0", server_port=10000)
