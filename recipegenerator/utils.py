import openai
import os
from decouple import config  # make sure python-decouple is installed

# Set DeepInfra as the base API
openai.api_base = "https://api.deepinfra.com/v1/openai"
openai.api_key = config("DEEPINFRA_API_KEY")
  # securely load from .env

def generate_recipe(ingredients):
    prompt = f"Create a unique recipe using: {ingredients}"

    response = openai.ChatCompletion.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
