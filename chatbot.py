import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a chat model
model = genai.GenerativeModel("models/gemma-3n-e2b-it")
chat = model.start_chat(history=[])

def respond(user_input, history):
    user_input_lower = user_input.lower()

    # Custom identity response
    if "who are you" in user_input_lower or "your name" in user_input_lower:
        custom_response = "I'm ROLLS — your personal AI assistant, created by Siddharth."
        history.append((user_input, custom_response))
        return history, history
    
    # Use Gemini for all other inputs
    response = chat.send_message(user_input)
    history.append((user_input, response.text))
    return history, history


# ✅ Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Gemini Chatbot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask something...")
    state = gr.State([])

    msg.submit(respond, inputs=[msg, state], outputs=[chatbot, state])
    
demo.launch()
