import ftplib
import os

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
LOCAL_FILE = 'whatsapp-bot-new/test.js'
REMOTE_FILE = 'www/server.js'

def upload():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"📤 Uploading {LOCAL_FILE} to {REMOTE_FILE}...")
        with open(LOCAL_FILE, 'rb') as f:
            ftp.storbinary(f'STOR {REMOTE_FILE}', f)
        print("✅ Upload successful!")
        ftp.quit()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    upload()
