import ftplib

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
REMOTE_DIR = 'admin'

def list_admin():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"📁 Listing {REMOTE_DIR}...")
        files = []
        ftp.retrlines(f'LIST {REMOTE_DIR}', files.append)
        for f in files:
            print(f)
        
        ftp.quit()

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    list_admin()
