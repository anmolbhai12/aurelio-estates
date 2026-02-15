import ftplib
import time

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def hard_restart_root():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # Root is where we land
        print("Uploading restart.txt to LOGIN ROOT...")
        with open('restart.txt', 'w') as f:
            f.write(str(time.time()))
            
        with open('restart.txt', 'rb') as f:
            ftp.storbinary('STOR restart.txt', f)
            
        # Also try tmp/restart.txt
        try:
            print("Uploading to tmp/restart.txt...")
            with open('restart.txt', 'rb') as f:
                ftp.storbinary('STOR tmp/restart.txt', f)
        except:
            pass
            
        ftp.quit()
        print("Done.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    hard_restart_root()
