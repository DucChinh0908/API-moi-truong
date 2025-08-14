# I. Cài đặt API ⚙
* Vào https://render.com/ → đăng ký bằng GitHub.
* Nhấn New → Web Service.
* Chọn repo bạn vừa push (hoặc sử dụng repo của mình và đổi tên API ở phần Name).
* Chọn environment: Python 3.x.
* Build Command:
```
pip install -r requirements.txt
```
* Start Command:
```
gunicorn app:app --bind 0.0.0.0:$PORT
```
* Nhấn Create Web Service và đợi vài phút.
* Sau khi deploy xong, Render sẽ cấp cho bạn một đường dẫn API dạng:
```
https://{tên-API}.onrender.com
```
# II. Sử dụng API 🛠
## 1. GET API
* Lấy dữ liệu môi trường
```
# Python
import requests
import time

url = "https://{tên-API}.onrender.com/api/data/environment"

while True:
    response = requests.get(url)
    print(response.json())
    time.sleep(1)
```
```
// JavaScript
const url = "https://{tên-API}.onrender.com/api/data/environment";
setInterval(async () => {
  try {
    const data = await (await fetch(url)).json();
    console.log(data);
  } catch (e) { console.error(e); }
}, 1000);
```
* Lấy dữ liệu cài đặt
```
# Python
import requests
import time

url = "https://{tên-API}.onrender.com/api/data/settings"

while True:
    response = requests.get(url)
    print(response.json())
    time.sleep(1)
```
```
// JavaScript
const url = "https://{tên-API}.onrender.com/api/data/settings";
setInterval(async () => {
  try {
    const data = await (await fetch(url)).json();
    console.log(data);
  } catch (e) { console.error(e); }
}, 1000);
2. POST API
```
* Gửi dữ liệu môi trường lên API
```
# Python
import requests
import random
import time

url = "https://{tên-API}.onrender.com/api/data/environment"

while True:
    data = {
        "temperature": random.randint(20, 40),
        "humidity": random.randint(20, 40),
        "water_level": random.randint(20, 40),
        "soil_moisture": random.randint(0, 1)
    }
    response = requests.post(url, json=data)
    print("Status:", response.status_code, "Response:", response.text)
    time.sleep(1)
```
```
// JavaScript
const url = "https://{tên-API}.onrender.com/api/data/environment";
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
setInterval(() => {
  const data = {
    temperature: randomInt(20, 40),
    humidity: randomInt(20, 40),
    water_level: randomInt(20, 40),
    soil_moisture: randomInt(0, 1)
  };
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => console.log("Status:", res.status))
  .catch(err => console.error("Error:", err));
}, 1000);
```
* Gửi cài đặt môi trường lên API
```
# Python
import requests
import random
import time

url = "https://{tên-API}.onrender.com/api/data/settings"

while True:
    value = {
        "min_temperature": random.randint(20, 40),
        "max_temperature": random.randint(20, 40),
        "min_humidity": random.randint(20, 40),
        "max_humidity": random.randint(20, 40)
    }
    response = requests.post(url, json=value)
    print("Status:", response.status_code, "Response:", response.text)
    time.sleep(1)
```
```
// JavaScript
const url = "https://{tên-API}.onrender.com/api/data/settings";
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
setInterval(() => {
  const value = {
    min_temperature: randomInt(20, 40),
    max_temperature: randomInt(20, 40),
    min_humidity: randomInt(20, 40),
    max_humidity: randomInt(20, 40)
  };
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(value)
  })
  .then(res => console.log("Status:", res.status))
  .catch(err => console.error("Error:", err));
}, 1000);
```
# III. Lời kết 📝
* Xin chào mọi người đây là một dự án API nhỏ trong hệ thống nông nghiệp thông minh. Sắp tới mình sẽ đưa toàn bộ dự án lên GitHub, mong được mọi người sử dụng và nhận được góp ý để cải thiện hệ thống tốt hơn. Cảm ơn các bạn đã sử dụng dự án của mình.
# IV. Thông tin liên hệ 📞
* Gmail: Kinerno2008@gmail.com
* Facebook: https://www.facebook.com/DucwsChi
