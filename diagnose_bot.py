import ftplib
import os
import sys

# --- CONFIGURATION ---
HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'
REMOTE_DIR = 'www'

def get_file_list(ftp, path):
    try:
        files = []
        ftp.cwd(path)
        ftp.retrlines('LIST', files.append)
        return files
    except Exception as e:
        return [f"Error listing {path}: {str(e)}"]

def diagnose():
    try:
        print(f"🕵️ Connecting to {HOST} for diagnosis...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        # 1. Check for node_modules in www
        print("\n📂 Checking 'www' folder contents...")
        www_files = get_file_list(ftp, '/www')
        node_modules_found = any('node_modules' in f for f in www_files)
        
        for f in www_files:
            print(f" - {f}")

        if not node_modules_found:
            print("\n❌ CRITICAL: 'node_modules' folder is MISSING!")
            print("   This confirms the server cannot start because libraries are not installed.")
        else:
            print("\n✅ 'node_modules' folder found.")

        # 2. Check for logs and READ them
        print("\n📜 Checking 'admin/logs/sites/'...")
        logs_path = '/admin/logs/sites/'
        try:
            ftp.cwd(logs_path)
            log_files = []
            ftp.retrlines('LIST', log_files.append)
            
            latest_log = None
            for f in log_files:
                print(f" - {f}")
                # Try to parse filename to find the latest .log file
                parts = f.split()
                if len(parts) >= 9:
                    filename = parts[-1]
                    if filename.endswith('.log'):
                        latest_log = filename

            if latest_log:
                print(f"\n📖 Reading latest log: {latest_log}...")
                
                # Define a callback to print lines
                def print_line(line):
                    print(line)

                # Retrieve the file content
                ftp.retrlines(f'RETR {latest_log}', print_line)
            else:
                print("   No .log files found to read.")

        except Exception as e:
            print(f"   Could not access or read logs: {str(e)}")

        ftp.quit()
        
    except Exception as e:
        print(f"\n❌ Error during diagnosis: {str(e)}")

if __name__ == "__main__":
    diagnose()
