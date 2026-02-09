import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_FILE = 'admin/logs/sites/2026/sites-2026-02-09.log'
LOCAL_FILE = 'sites-today-new.log'

def download_log():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"Downloading {REMOTE_FILE}...")
        with open(LOCAL_FILE, 'wb') as f:
            ftp.retrbinary(f'RETR {REMOTE_FILE}', f.write)
        print("Download successful!")
        
        ftp.quit()

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    download_log()
