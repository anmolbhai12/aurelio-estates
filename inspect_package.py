import ftplib
import json

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def inspect_package_json():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        print("Downloading package.json for inspection...")
        with open('package_inspect.json', 'wb') as f:
            ftp.retrbinary('RETR package.json', f.write)
            
        with open('package_inspect.json', 'r') as f:
            data = json.load(f)
            print("MAIN:", data.get('main'))
            print("SCRIPTS:", data.get('scripts'))
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_package_json()
