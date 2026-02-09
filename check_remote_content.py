import ftplib
import os

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def check_remote_content():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("\n--- Checking www/package.json ---")
        try:
            with open('remote_package.json', 'wb') as f:
                ftp.retrbinary('RETR www/package.json', f.write)
            with open('remote_package.json', 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Failed to read package.json: {e}")

        print("\n--- Checking www/server.js Head ---")
        try:
            with open('remote_server.js', 'wb') as f:
                ftp.retrbinary('RETR www/server.js', f.write)
            with open('remote_server.js', 'r') as f:
                print(f.read(500)) # Print first 500 chars
        except Exception as e:
            print(f"Failed to read server.js: {e}")

        ftp.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_remote_content()
