import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
from openai import OpenAI

def load_model(model_name):
    if model_name in ["gpt4-o", "gpt3.5"]:
        return None, None  # Placeholder for API-based models
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer


client = OpenAI(
    api_key="INSERT_KEY",
)

def get_gpt35_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo" ,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_gpt4o_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o" ,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
