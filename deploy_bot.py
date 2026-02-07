import ftplib
import os

# --- CONFIGURATION ---
HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'  # <--- ENTER YOUR ALWAYSDATA PASSWORD HERE
REMOTE_DIR = 'www'
LOCAL_DIR = 'whatsapp-bot'

def upload_files():
    try:
        print(f"🚀 Connecting securely to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p() # Secure the data channel (Required by Alwaysdata)
        
        # Change to the www directory
        ftp.cwd(REMOTE_DIR)
        print(f"📂 Entered remote directory: {REMOTE_DIR}")

        # Files to upload
        files_to_upload = ['package.json', 'package-lock.json', 'server.js', 'whatsapp.js', '.gitignore', 'README.md']
        
        for filename in files_to_upload:
            local_path = os.path.join(LOCAL_DIR, filename)
            if os.path.exists(local_path):
                print(f"📤 Uploading {filename}...")
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
            else:
                print(f"⚠️ Skipping {filename} (not found locally)")

        ftp.quit()
        print("\n✅ SUCCESS! All items uploaded to your new bot.")
        print(f"👉 Visit http://aurelio-bot.publicvm.com/status to scan your QR code.")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("💡 Make sure your password is correct and your Alwaysdata site is active.")

if __name__ == "__main__":
    upload_files()
