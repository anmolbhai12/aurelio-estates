import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def list_and_download_logs():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # List admin/logs/sites
        try:
            print("Listing admin/logs/sites...")
            ftp.cwd('admin/logs/sites')
            files = ftp.nlst()
            print(f"Files in sites/: {files}")
            for name in files:
                if name.endswith('.log'):
                    print(f"Downloading {name}...")
                    with open(f"site_{name}", 'wb') as f:
                        ftp.retrbinary(f'RETR {name}', f.write)
        except Exception as e:
            print(f"Error in sites/: {e}")

        # List admin/logs/http
        try:
            ftp.cwd('../../http') # Back to admin/logs, then into http
            print("Listing admin/logs/http...")
            files = ftp.nlst()
            print(f"Files in http/: {files}")
            for name in files:
                if name.endswith('.log'):
                    print(f"Downloading {name}...")
                    with open(f"http_{name}", 'wb') as f:
                        ftp.retrbinary(f'RETR {name}', f.write)
        except Exception as e:
            print(f"Error in http/: {e}")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    list_and_download_logs()
