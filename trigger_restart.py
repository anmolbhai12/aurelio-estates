import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def trigger_restart():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # Method 1: Upload restart.txt to www
        print("Creating www/restart.txt...")
        with open('restart.txt', 'w') as f:
            f.write('restart')
            
        with open('restart.txt', 'rb') as f:
            ftp.storbinary('STOR www/restart.txt', f)
            
        # Method 2: Try to create tmp/restart.txt (if access allowed)
        try:
            print("Attempting to create tmp/restart.txt in root...")
            ftp.cwd('..') # Go up
            if 'tmp' not in ftp.nlst():
                try:
                    ftp.mkd('tmp')
                except:
                    pass
            
            ftp.cwd('tmp')
            with open('restart.txt', 'rb') as f:
                ftp.storbinary('STOR restart.txt', f)
            print("Uploaded tmp/restart.txt")
        except Exception as e:
            print(f"Could not upload to root/tmp: {e}")

        ftp.quit()
        print("Restart triggers deployed.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    trigger_restart()
