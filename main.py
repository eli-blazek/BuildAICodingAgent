import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



try:
    proompt = sys.argv[1]
except IndexError:
    sys.exit("No prompt provided")

messages = [
        types.Content(role="user", parts=[types.Part(text=proompt)]),
    ]
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=messages
)

try:
    if sys.argv[2] == "--verbose" or sys.argv[2] == "-v":
            print(f"User prompt: {proompt} \nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")
            print(response.text)
except IndexError:
    print(response.text)