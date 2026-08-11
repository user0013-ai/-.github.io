import base64, os

img_path = r"C:\Users\ASUS\Desktop\test\avatar.jpg.jpg"
html_path = r"C:\Users\ASUS\Desktop\test\index.html"

if not os.path.isfile(img_path):
    alt = r"C:\Users\ASUS\Desktop\test\avatar.jpg"
    if os.path.isfile(alt):
        img_path = alt
    else:
        print("ERROR: avatar image not found")
        exit(1)

with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

data_uri = "data:image/jpeg;base64," + b64

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace(
    'src="https://s41.ax1x.com/2026/08/11/pmqS9fg.jpg"',
    'src="' + data_uri + '"'
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
print("Base64 length:", len(b64), "chars")
print("HTML file is now fully self-contained.")