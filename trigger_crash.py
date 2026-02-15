import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def trigger_crash_restart():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www/auth_info')
        
        # Try to delete creds.json to trigger the crash loop
        try:
            print("Deleting creds.json...")
            ftp.delete('creds.json')
            print("Deleted.")
        except:
            print("creds.json not found or already deleted.")
            
        ftp.quit()
        print("Crash trigger attempt complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    trigger_crash_restart()
