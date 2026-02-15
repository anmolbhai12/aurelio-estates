import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def check_remote_index():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        print("Downloading index.html...")
        with open('index_check.html', 'wb') as f:
            ftp.retrbinary('RETR index.html', f.write)
            
        with open('index_check.html', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'v5.0' in content: # Checking for the version tag I added
                print("Found v5.0 in remote index.html")
            if 'v4.0' in content:
                print("Found v4.0 in remote index.html")
            else:
                print("No version tag found in remote index.html")
                
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_remote_index()
