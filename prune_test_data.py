import ftplib
import json
import io

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_FILE = 'www/properties.json'

def prune_test_data():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # 1. Download properties.json
        print(f"Reading {REMOTE_FILE}...")
        bio = io.BytesIO()
        ftp.retrbinary(f'RETR {REMOTE_FILE}', bio.write)
        bio.seek(0)
        properties = json.load(bio)
        
        # 2. Filter out IDs 1, 2, 3 (Test entries)
        original_count = len(properties)
        # We prune ID 1, 2, 3 as seen in our research
        clean_properties = [p for p in properties if p.get('id') not in [1, 2, 3]]
        
        print(f"Pruned {original_count - len(clean_properties)} test entries.")
        
        # 3. Upload cleaned file
        print(f"Uploading cleaned {REMOTE_FILE}...")
        cleaned_json = json.dumps(clean_properties, indent=2)
        cleaned_bio = io.BytesIO(cleaned_json.encode('utf-8'))
        ftp.storbinary(f'STOR {REMOTE_FILE}', cleaned_bio)
        
        ftp.quit()
        print("\nDATABASE CLEANUP COMPLETE!")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    prune_test_data()
