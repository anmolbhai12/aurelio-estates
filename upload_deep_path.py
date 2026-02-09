import ftplib
import os

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
LOCAL_DIR = 'whatsapp-bot-new'
REMOTE_DIR = 'home/aurelio-bot/www'

def upload_deep():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"📤 Uploading to {REMOTE_DIR}...")
        files_to_upload = ['server.js', 'package.json', 'package-lock.json']
        
        for file in files_to_upload:
            local_path = os.path.join(LOCAL_DIR, file)
            if os.path.exists(local_path):
                print(f"   - Uploading {file}...")
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {REMOTE_DIR}/{file}', f)
            else:
                print(f"   - Skipping {file} (not found locally)")
        
        print("✅ Upload complete.")
        ftp.quit()

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    upload_deep()
