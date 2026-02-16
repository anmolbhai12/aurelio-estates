import ftplib
import os
import time

# Unified Deployment Script for Tha
HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def upload_folder(ftp, local_path, remote_path):
    print(f"Uploading {local_path} to {remote_path}...")
    for item in os.listdir(local_path):
        local_item = os.path.join(local_path, item)
        # Use forward slashes for FTP paths
        remote_item = f"{remote_path}/{item}"
        
        if os.path.isfile(local_item):
            with open(local_item, 'rb') as f:
                ftp.storbinary(f'STOR {remote_item}', f)
            print(f"  - Uploaded {item}")
        elif os.path.isdir(local_item):
            try:
                ftp.mkd(remote_item)
            except ftplib.error_perm:
                pass
            upload_folder(ftp, local_item, remote_item)

def deploy():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # 1. Upload Backend
        backend_files = {
            'whatsapp-bot-new/server.js': 'www/server.js',
            'whatsapp-bot-new/whatsapp.js': 'www/whatsapp.js'
        }
        for local_p, remote_p in backend_files.items():
            if os.path.exists(local_p):
                print(f"Uploading {local_p} -> {remote_p}")
                with open(local_p, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_p}', f)
        
        # 2. Upload Frontend (dist folder)
        if os.path.exists('dist'):
            print("Uploading Frontend (dist)...")
            upload_folder(ftp, 'dist', 'www')
        
        # 3. Aggressive Restart (Rename trick)
        print("Performing aggressive restart...")
        try:
            ftp.cwd('www')
            ftp.rename('server.js', 'server.js.tmp')
            time.sleep(3)
            ftp.rename('server.js.tmp', 'server.js')
            print("Restart triggered via rename!")
        except Exception as e:
            print(f"Restart rename failed (might not be needed if auto-restart active): {e}")

        ftp.quit()
        print("\nFULL DEPLOYMENT COMPLETE!")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    deploy()
