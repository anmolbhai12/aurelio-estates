import ftplib
import time

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def nuke_restart():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Renaming www to www_nuke...")
        ftp.rename('www', 'www_nuke')
        
        time.sleep(10)
        
        print("Renaming back to www...")
        ftp.rename('www_nuke', 'www')
        
        ftp.quit()
        print("Nuke restart complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    nuke_restart()
