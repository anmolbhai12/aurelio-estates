import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def download_file():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        with open('server_remote_ver.js', 'wb') as f:
            ftp.retrbinary('RETR server.js', f.write)
        print("Downloaded server.js as server_remote_ver.js")

        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {str(e)}")

if __name__ == "__main__":
    download_file()
