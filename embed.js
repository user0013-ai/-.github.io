const fs = require('fs');
const b = fs.readFileSync('C:/Users/ASUS/Desktop/test/avatar.jpg.jpg');
const b64 = b.toString('base64');
const html = fs.readFileSync('C:/Users/ASUS/Desktop/test/index.html', 'utf8');
const out = html.replace('src="./avatar.jpg.jpg"', 'src="data:image/jpeg;base64,' + b64 + '"');
fs.writeFileSync('C:/Users/ASUS/Desktop/test/index.html', out);
console.log('OK, b64 len=' + b64.length);