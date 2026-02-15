import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def read_large_log():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Reading last 100 lines of boot.log...")
        lines = []
        ftp.retrlines('RETR www/boot.log', lines.append)
        
        print("--- LAST 100 LINES ---")
        for line in lines[-100:]:
            print(line)
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_large_log()
