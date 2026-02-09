import ftplib

HOST = 'ftp-aurelio-bot.alwaysdata.net'
USER = 'aurelio-bot'
PASS = 'dalaalstreets123'

def create_deep_structure():
    try:
        print(f"🚀 Connecting to {HOST}...")
        ftp = ftplib.FTP_TLS(HOST)
        ftp.login(USER, PASS)
        ftp.prot_p()
        
        folders = ['home', 'home/aurelio-bot', 'home/aurelio-bot/www']
        for folder in folders:
            try:
                print(f"📁 Creating {folder}...")
                ftp.mkd(folder)
                print(f"✅ Created {folder}")
            except Exception as e:
                print(f"⚠️ Could not create {folder} (maybe exists?): {e}")
        
        # Now upload server.js and package.json to the deep www
        # I'll use a simplified version of upload_test but for the deep path
        
        ftp.quit()

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    create_deep_structure()
