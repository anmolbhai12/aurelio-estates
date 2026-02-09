import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def list_remote_details():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("\n--- Listing WWW Directory ---")
        ftp.cwd('www')
        files = []
        ftp.retrlines('LIST', files.append)
        for f in files:
            print(f)
            
        print("\n--- Listing Assets Directory ---")
        try:
            ftp.cwd('assets')
            assets = []
            ftp.retrlines('LIST', assets.append)
            for a in assets:
                print(a)
        except:
            print("No assets directory found or accessible.")

        ftp.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    list_remote_details()
