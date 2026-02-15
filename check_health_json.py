import requests

URL = 'https://dalaalstreetss.alwaysdata.net/health'

try:
    response = requests.get(URL)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
