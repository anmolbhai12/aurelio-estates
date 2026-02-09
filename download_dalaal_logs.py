import ftplib
import sys

# Set encoding for Windows console to handle UTF-8 if possible, 
# but we will remove emojis to be safe.
HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
REMOTE_LOG_DIR = 'admin/logs'
LOCAL_LOG_FILE = 'sites-today.log'

def download_log():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        try:
            ftp.cwd('admin/logs')
            files = ftp.nlst()
            print(f"Log files found: {files}")
            
            log_name = 'site.log' if 'site.log' in files else files[0] if files else None
            
            if log_name:
                print(f"Downloading {log_name}...")
                with open(LOCAL_LOG_FILE, 'wb') as f:
                    ftp.retrbinary(f'RETR {log_name}', f.write)
                print(f"Downloaded to {LOCAL_LOG_FILE}")
            else:
                print("No log files found in admin/logs")
                
        except Exception as e:
            print(f"Error accessing admin/logs: {e}")
            print("Try checking 'www/boot.log' instead...")
            try:
                ftp.cwd('../../www') 
                with open('boot.log', 'wb') as f:
                    ftp.retrbinary('RETR boot.log', f.write)
                print("Downloaded boot.log from www/")
            except Exception as e2:
                print(f"Could not find boot.log in www/ either: {e2}")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    download_log()
