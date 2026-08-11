import base64, os

os.chdir(r"C:\Users\ASUS\Desktop\test")

for fn in ["avatar.jpg.jpg", "avatar.jpg"]:
    if os.path.isfile(fn):
        img_path = fn
        break
else:
    print("NO IMAGE FOUND")
    exit()

with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

old = 'src="https://s41.ax1x.com/2026/08/11/pmqS9fg.jpg"'
new = 'src="data:image/jpeg;base64,' + b64 + '"'

if old in html:
    html = html.replace(old, new)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: embedded", len(b64), "chars")
else:
    print("Pattern not found in HTML")
    print("Searching for src=...")
    import re
    m = re.search(r'src="([^"]+)"', html)
    if m:
        print("Found:", m.group(1)[:80])