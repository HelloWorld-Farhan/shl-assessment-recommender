import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    print("Testing /health endpoint...")
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {resp.status_code}")
    print(f"Response: {resp.json()}\n")

def test_chat():
    print("Testing /chat endpoint...")
    payload = {
        "messages": [
            {"role": "user", "content": "I am looking for an assessment for a mid-level Java developer."}
        ]
    }
    
    resp = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"Status Code: {resp.status_code}")
    print("Response:")
    print(json.dumps(resp.json(), indent=2))

if __name__ == "__main__":
    try:
        test_health()
        test_chat()
    except requests.exceptions.ConnectionError:
        print("Failed to connect. Make sure the FastAPI server is running with 'uvicorn main:app --reload'")
