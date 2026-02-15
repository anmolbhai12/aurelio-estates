import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def check_remote_server_js():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        print("Downloading server.js for inspection...")
        with open('server_check.js', 'wb') as f:
            ftp.retrbinary('RETR server.js', f.write)
            
        with open('server_check.js', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if '/server-logs' in content:
                print("✅ Found /server-logs in remote server.js")
            else:
                print("❌ /server-logs NOT FOUND in remote server.js")
                
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_remote_server_js()
