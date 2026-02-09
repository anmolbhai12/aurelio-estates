import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def download_service_logs():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        try:
            print("Listing admin/logs/services...")
            ftp.cwd('admin/logs/services')
            files = ftp.nlst()
            print(f"Files in services/: {files}")
            
            # Download the most recent ones
            for name in files:
                print(f"Downloading {name}...")
                with open(f"service_{name}.log", 'wb') as f:
                    ftp.retrbinary(f'RETR {name}', f.write)
        except Exception as e:
            print(f"Error in services/: {e}")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    download_service_logs()
