import requests

def query_llama3_ollama(category):
    prompt = f"What are the top 2 brands in the {category} industry and why are they popular?"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 150  # limits output to ~150 tokens
            }
        }
        
    )

    result = response.json()
    return result['response']
