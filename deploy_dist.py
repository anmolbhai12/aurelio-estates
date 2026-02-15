import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_DIR = 'www'
LOCAL_DIST = 'dist'

def upload_directory(ftp, local_path, remote_path):
    for item in os.listdir(local_path):
        l_item = os.path.join(local_path, item)
        r_item = remote_path + '/' + item
        
        if os.path.isfile(l_item):
            print(f"Uploading file: {r_item}")
            with open(l_item, 'rb') as f:
                ftp.storbinary(f'STOR {r_item}', f)
        elif os.path.isdir(l_item):
            print(f"Entering directory: {r_item}")
            try:
                ftp.mkd(r_item)
            except:
                pass
            upload_directory(ftp, l_item, r_item)

def deploy_full_dist():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # Deploy dist contents to www root
        upload_directory(ftp, LOCAL_DIST, REMOTE_DIR)
        
        ftp.quit()
        print("Full deployment to AlwaysData complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    deploy_full_dist()
