import ftplib
import os

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
LOCAL_DIR = 'whatsapp-bot-new'

def upload_step_by_step():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        path_segments = ['home', 'aurelio-bot', 'www']
        for segment in path_segments:
            try:
                print(f"📂 Entering {segment}...")
                ftp.cwd(segment)
            except:
                print(f"📁 Creating {segment}...")
                ftp.mkd(segment)
                ftp.cwd(segment)
        
        print(f"📍 Current Directory: {ftp.pwd()}")
        
        files_to_upload = ['server.js', 'package.json', 'package-lock.json']
        for file in files_to_upload:
            local_path = os.path.join(LOCAL_DIR, file)
            if os.path.exists(local_path):
                print(f"   - Uploading {file}...")
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {file}', f)
        
        print("✅ Upload complete.")
        ftp.quit()

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    upload_step_by_step()
