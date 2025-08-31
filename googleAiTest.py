# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import google.generativeai as genai
# from google import genai
from google.generativeai import types



def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemma-3n-e2b-it"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""tell me about taj mahal"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""write a resignation email to boss"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
