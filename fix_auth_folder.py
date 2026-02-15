import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def fix_auth_folder():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        try:
            ftp.cwd('auth_info')
            print("auth_info directory exists.")
        except:
            print("Creating auth_info directory...")
            ftp.mkd('auth_info')
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_auth_folder()
