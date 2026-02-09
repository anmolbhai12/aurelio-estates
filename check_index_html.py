import ftplib

HOST = 'ftp-dalaalstreetss.alwaysdata.net'
USER = 'dalaalstreetss'
PASS = 'dalaalstreets123'

def check_index_html():
    try:
        print(f"Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        print("\n--- Checking www/index.html ---")
        try:
            with open('remote_index.html', 'wb') as f:
                ftp.retrbinary('RETR www/index.html', f.write)
            with open('remote_index.html', 'r') as f:
                content = f.read()
                print(content)
                if 'index-DYSjAlgw.js' in content:
                    print("\n✅ SUCCESS: index.html points to the latest JS bundle (v2.8).")
                else:
                    print("\n❌ FAILURE: index.html points to an older JS bundle.")
        except Exception as e:
            print(f"Failed to read index.html: {e}")

        ftp.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_index_html()
