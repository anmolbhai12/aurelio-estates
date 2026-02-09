import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_FILE = 'www/boot.log'
LOCAL_FILE = 'boot.log'

def download():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Downloading boot.log from www...")
        with open('boot.log', 'wb') as f:
            ftp.retrbinary('RETR www/boot.log', f.write)
        print("Done!")
        
        ftp.quit()

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    download()
