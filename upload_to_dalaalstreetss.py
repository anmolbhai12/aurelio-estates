import os
import ftplib

# FTP Credentials
HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_DIR = 'www'
LOCAL_DIR = 'whatsapp-bot-new'

def upload_files(ftp):
    print(f"Uploading bot files from {LOCAL_DIR} to {REMOTE_DIR}...")
    
    # Ensure remote directory exists
    try:
        ftp.cwd(REMOTE_DIR)
    except:
        print(f"Creating remote directory {REMOTE_DIR}...")
        ftp.mkd(REMOTE_DIR)
        ftp.cwd(REMOTE_DIR)

    if not os.path.exists(LOCAL_DIR):
        print(f"Local dir {LOCAL_DIR} not found!")
        return

    for file in os.listdir(LOCAL_DIR):
        # Skip node_modules and other large/private items
        if file in ['node_modules', '.git', 'auth_info', 'boot.log', '.env', 'package-lock.json']:
            continue
            
        local_path = os.path.join(LOCAL_DIR, file)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                print(f"   - Uploading {file}...")
                ftp.storbinary(f'STOR {file}', f)
    print("Upload complete.")

def main():
    try:
        print(f"Connecting to {HOST} as {USER}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p() # Secure the connection
        
        upload_files(ftp)
        
        ftp.quit()
        print("Done!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
