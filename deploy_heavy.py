import ftplib
import os
import shutil
import zipfile

# --- CONFIGURATION ---
HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
REMOTE_DIR = 'www'
LOCAL_DIR = r'c:\Users\DELL\Desktop\New folder\whatsapp-bot'

def zip_folder(folder_path, output_path):
    print(f"📦 Zipping {folder_path}...")
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Calculate length of path to replace for relative paths
        len_dir_path = len(os.path.dirname(folder_path))
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Keep directory structure relative to folder_path
                archive_name = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, archive_name)
    print(f"✅ Created {output_path}")

def deploy():
    try:
        # 1. Zip node_modules
        node_modules_path = os.path.join(LOCAL_DIR, 'node_modules')
        zip_path = os.path.join(LOCAL_DIR, 'node_modules.zip')
        
        if not os.path.exists(node_modules_path):
            print("❌ node_modules not found locally! Run 'npm install' first.")
            return

        zip_folder(node_modules_path, zip_path)

        # 2. Upload
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"📂 Entering {REMOTE_DIR}...")
        try:
            ftp.cwd(REMOTE_DIR)
        except:
            print(f"❌ Could not find {REMOTE_DIR}, creating it...")
            ftp.mkd(REMOTE_DIR)
            ftp.cwd(REMOTE_DIR)

        print(f"📤 Uploading node_modules.zip ({os.path.getsize(zip_path) / 1024 / 1024:.2f} MB)...")
        with open(zip_path, 'rb') as file:
            ftp.storbinary(f'STOR node_modules.zip', file)
        
        print("\n✅ Upload Complete!")
        print("👉 Now go to your SSH terminal and run:")
        print("   unzip node_modules.zip && npm start")

        ftp.quit()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    deploy()
