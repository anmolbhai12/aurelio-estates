import requests
import json

URL = 'https://dalaalstreetss.alwaysdata.net/properties'

def test_upload_ordered():
    print(f"Testing upload to {URL}...")
    
    payload = {
        'title': 'Ordered Upload Test',
        'location': 'Debug City',
        'price': 500,
        'mobile': '9999999999',
        'seller': 'DebugBot',
        'verified': True
    }
    
    # Construct multipart manually to control order?
    # Requests 'files' param can take a list of tuples to enforce order.
    # (field_name, (filename, file_content, content_type))
    # OR (field_name, value) for text fields.
    
    multipart_data = [
        ('data', (None, json.dumps(payload), 'application/json')), 
        ('media', ('test_video.mp4', open('test_video.mp4', 'rb'), 'video/mp4'))
    ]
    
    try:
        response = requests.post(URL, files=multipart_data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_upload_ordered()
