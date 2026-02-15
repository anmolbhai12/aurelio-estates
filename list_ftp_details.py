import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def list_root():
    print(f"Connecting to {HOST}...")
    try:
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("Listing root (relative to login):")
        print(ftp.nlst())
        
        try:
            print("Listing 'www':")
            print(ftp.nlst('www'))
        except:
            pass
            
        try:
            print("Contents of 'www/boot.log' (last 20 lines):")
            lines = []
            ftp.retrlines('RETR www/boot.log', lines.append)
            for line in lines[-20:]:
                print(line)
        except Exception as e:
            print(f"Error reading log: {e}")
            
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_root()
