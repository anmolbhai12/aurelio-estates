import ftplib
import time

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def aggressive_rename_restart():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        ftp.cwd('www')
        
        print("Renaming server.js to server.js.off...")
        ftp.rename('server.js', 'server.js.off')
        
        time.sleep(5)
        
        print("Renaming back to server.js...")
        ftp.rename('server.js.off', 'server.js')
        
        ftp.quit()
        print("Aggressive rename complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    aggressive_rename_restart()
