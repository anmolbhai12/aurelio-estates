import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def download_and_print_log():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        print("Downloading boot.log...")
        with open('latest_boot.log', 'wb') as f:
            ftp.retrbinary('RETR boot.log', f.write)
            
        print("--- LAST 200 LINES of boot.log ---")
        with open('latest_boot.log', 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for line in lines[-200:]:
                print(line.strip())
                
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_and_print_log()
