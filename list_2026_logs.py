import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def list_2026_logs():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Downloading site logs...")
        ftp.cwd('admin/logs/sites/2026')
        files = ftp.nlst()
        for name in files:
            with open(f"log_2026_{name}", 'wb') as f:
                ftp.retrbinary(f'RETR {name}', f.write)
        print("Done!")
        ftp.quit()
    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    list_2026_logs()
