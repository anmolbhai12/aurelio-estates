import ftplib
import json

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def finalize_deploy():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        # 1. Update package.json back to server.js
        print("Downloading package.json...")
        with open('package_final.json', 'wb') as f:
            ftp.retrbinary('RETR package.json', f.write)
            
        with open('package_final.json', 'r') as f:
            data = json.load(f)
            
        data['main'] = 'server.js'
        data['scripts']['start'] = 'node server.js'
        
        # Random version bump for restart
        old_v = data.get('version', '4.0.2')
        data['version'] = old_v + '.final'
        
        with open('package_final.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print("Uploading final package.json...")
        with open('package_final.json', 'rb') as f:
            ftp.storbinary('STOR package.json', f)
            
        # 2. Upload fixed server.js
        print("Uploading server.js...")
        with open('whatsapp-bot-new/server.js', 'rb') as f:
            ftp.storbinary('STOR server.js', f)
            
        ftp.quit()
        print("Final deployment steps complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    finalize_deploy()
