import requests

URL = 'https://dalaalstreetss.alwaysdata.net/health'

try:
    response = requests.get(URL)
    print("--- HEADERS ---")
    for k, v in response.headers.items():
        print(f"{k}: {v}")
except Exception as e:
    print(f"Error: {e}")
