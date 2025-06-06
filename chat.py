import requests
import ollama
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "carlos:latest"

def get_user_prompt():
    """Get prompt input from Chili admirer"""
    return (input("Enter your prompt beautiful ;) : "))


def get_payload(prompt):
    """Generate a payload for the prompt"""
    data =  {
        "model" : MODEL_NAME,
        "prompt" : prompt
    }
    return data

def get_response(payload):
    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    #checking response status
    if response.status_code == 200:
        print("Chili wants to say that : \n", end=" ", flush=True)
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                result = json.loads(decoded_line)
                generated_text = result.get("response", "")
                print(generated_text, end="", flush=True)

    else:
        print("Error :", response.status_code, response.text)


def main():
    prompt = get_user_prompt()
    payload = get_payload(prompt)
    get_response(payload)

if __name__ == "__main__":
    main()