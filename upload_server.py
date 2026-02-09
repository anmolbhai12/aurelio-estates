import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def upload_server():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        local_path = r'c:\Users\DELL\Desktop\New folder\whatsapp-bot-new\server.js'
        remote_path = 'www/server.js'
        
        print(f"Uploading {local_path} to {remote_path}...")
        with open(local_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)
            
        print("Upload complete. Server should restart automatically.")
        ftp.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    upload_server()
