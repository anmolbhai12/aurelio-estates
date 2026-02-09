import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def download_2026_services():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        try:
            print("Listing admin/logs/services/2026...")
            ftp.cwd('admin/logs/services/2026')
            files = ftp.nlst()
            print(f"Files in services/2026: {files}")
            
            for name in files:
                print(f"Downloading {name}...")
                with open(f"service_log_2026_{name}", 'wb') as f:
                    ftp.retrbinary(f'RETR {name}', f.write)
        except Exception as e:
            print(f"Error in services/2026: {e}")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    download_2026_services()
