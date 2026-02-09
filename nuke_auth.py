import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'
TARGET_DIR = 'www/auth_info'

def nuke_dir(ftp, path):
    try:
        files = ftp.nlst(path)
    except ftplib.error_perm:
        return

    for item in files:
        if item in ['.', '..']:
            continue
        try:
            ftp.delete(item)
            print(f"Deleted: {item}")
        except ftplib.error_perm:
            nuke_dir(ftp, item)
    
    try:
        ftp.rmd(path)
        print(f"Removed directory: {path}")
    except Exception as e:
        print(f"Could not remove {path}: {e}")

def main():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print(f"Nuking {TARGET_DIR}...")
        nuke_dir(ftp, TARGET_DIR)
        
        ftp.quit()
        print("Done!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
