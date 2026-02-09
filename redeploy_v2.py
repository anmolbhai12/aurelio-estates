import ftplib
import os

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
LOCAL_DIR = 'whatsapp-bot-new'
REMOTE_DIR = 'www'

def wipe_remote(ftp):
    try:
        print(f"🗑️ Wiping {REMOTE_DIR}...")
        try:
            ftp.cwd(REMOTE_DIR)
            files = []
            ftp.retrlines('LIST', files.append)
            for f in files:
                name = f.split()[-1]
                if name in ['.', '..']: continue
                
                # Try delete as file first
                try:
                   ftp.delete(name)
                   print(f"   Deleted file: {name}")
                except:
                   # Try as directory (simple)
                   try:
                       ftp.rmd(name)
                       print(f"   Deleted dir: {name}")
                   except:
                       print(f"   Skipped/Failed: {name}")

            ftp.cwd('..') 
        except Exception as e:
             print(f"   Error listing/entering www: {e}")
        print("✅ Wipe complete (best effort).")
    except Exception as e:
        print(f"⚠️ Wipe warning: {e}")

def upload_new(ftp):
    print(f"📤 Uploading new bot from {LOCAL_DIR}...")
    ftp.cwd(REMOTE_DIR)
    if not os.path.exists(LOCAL_DIR):
        print(f"❌ Local dir {LOCAL_DIR} not found!")
        return

    for file in os.listdir(LOCAL_DIR):
        local_path = os.path.join(LOCAL_DIR, file)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as f:
                print(f"   - Uploading {file}...")
                ftp.storbinary(f'STOR {file}', f)
    print("✅ Upload complete.")

def main():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        wipe_remote(ftp)
        upload_new(ftp)
        
        ftp.quit()
        print("\n✨ Ready for 'npm install' & 'npm start'!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
