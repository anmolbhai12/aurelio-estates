import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def upload_folder(ftp, local_path, remote_path):
    print(f"Uploading {local_path} to {remote_path}...")
    for item in os.listdir(local_path):
        local_item = os.path.join(local_path, item)
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

def main():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # Upload dist contents to www
        upload_folder(ftp, 'dist', 'www')
        
        ftp.quit()
        print("Upload complete. Done!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
