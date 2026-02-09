import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
# I'll use the credentials I have
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def list_remote_files():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Listing contents of 'www'...")
        ftp.cwd('www')
        files = ftp.nlst()
        print(f"Files in www/: {files}")
        
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_remote_files()
