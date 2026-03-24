import argparse
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client  = genai.Client(api_key=api_key)



parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

user_prompt = args.user_prompt

response = client.models.generate_content(
    model="gemma-3-1b-it", contents=user_prompt)



print(f"user prompt: {user_prompt}")
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(f"Response: {response.text}")