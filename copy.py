import shutil, os

src = r"C:\Users\ASUS\Downloads\_cgi-bin_mmwebwx-bin_webwxgetmsgimg__&MsgID=3089672732451922057&skey=@crypt_8ed68494_9e28f9b93730f2ff3e9a9725845b53ed&mmweb_appid=wx_webfilehelper.jpg"
dst = r"C:\Users\ASUS\Desktop\test\avatar.jpg"

if os.path.isfile(src):
    shutil.copy2(src, dst)
    size = os.path.getsize(dst)
    print(f"OK: copied {size} bytes")
else:
    print(f"FAILED: source not found")
    print(os.listdir(r"C:\Users\ASUS\Downloads")[:5])