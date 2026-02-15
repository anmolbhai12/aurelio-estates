import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_FILE = 'www/boot.log'
LOCAL_FILE = 'boot_downloaded.log'

def download_log():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # List files to be sure
        files = ftp.nlst('www')
        if 'boot.log' in files: # Check relative path if needed, nlst returns names
             pass 

        print(f"Downloading {REMOTE_FILE}...")
        with open(LOCAL_FILE, 'wb') as f:
            ftp.retrbinary(f'RETR {REMOTE_FILE}', f.write)
            
        print("Download complete.")
        
        # Read and print last 50 lines
        with open(LOCAL_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            print("--- LAST 50 LINES ---")
            print(''.join(lines[-50:]))
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_log()
