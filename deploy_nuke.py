import ftplib
import json

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def nuke_deploy():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        # 1. Upload nuke_8100.js
        print("Uploading nuke_8100.js...")
        with open('nuke_8100.js', 'rb') as f:
            ftp.storbinary('STOR nuke_8100.js', f)
            
        # 2. Update package.json
        print("Downloading package.json...")
        with open('package_nuke.json', 'wb') as f:
            ftp.retrbinary('RETR package.json', f.write)
            
        with open('package_nuke.json', 'r') as f:
            data = json.load(f)
            
        data['main'] = 'nuke_8100.js'
        data['scripts']['start'] = 'node nuke_8100.js'
        
        with open('package_nuke.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print("Uploading updated package.json (Nuke mode)...")
        with open('package_nuke.json', 'rb') as f:
            ftp.storbinary('STOR package.json', f)
            
        ftp.quit()
        print("Nuke deployment complete. Triggering restart...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    nuke_deploy()
