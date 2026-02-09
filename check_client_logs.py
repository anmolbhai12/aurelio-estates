import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def check_client_logs():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("\n--- Checking client_debug.log ---")
        try:
            filename = 'www/client_debug.log'
            if 'client_debug.log' in ftp.nlst('www'):
                with open('local_client_debug.log', 'wb') as f:
                    ftp.retrbinary(f'RETR {filename}', f.write)
                with open('local_client_debug.log', 'r') as f:
                    print(f.read())
            else:
                print("No client_debug.log found yet.")
        except Exception as e:
            print(f"Failed to read log: {e}")

        ftp.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_client_logs()
