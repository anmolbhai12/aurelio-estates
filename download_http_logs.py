import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def download_http_logs():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        try:
            print("Listing admin/logs/http...")
            ftp.cwd('admin/logs/http')
            files = ftp.nlst()
            print(f"Files in http/: {files}")
            
            for name in files:
                if 'access' in name:
                    print(f"Downloading {name}...")
                    with open(f"http_{name}.log", 'wb') as f:
                        ftp.retrbinary(f'RETR {name}', f.write)
        except Exception as e:
            print(f"Error in http/: {e}")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    download_http_logs()
