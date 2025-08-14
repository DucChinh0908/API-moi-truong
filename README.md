# I.Cài đặt API ⚙
  * 1.Vào https://render.com/ → đăng ký bằng GitHub.
  * 2.Nhấn New → Web Service.
  * 3.Chọn repo bạn vừa push.
  * 4.Chọn environment: Python 3.x.
  * 5.Build Command: pip install -r requirements.txt
  * 6.Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
  * 7.Nhấn Create Web Service và đợi vài phút
  * 8.sau khi deploy xong Render sẽ cho các bạn 1 đường dẫn API có dạng : https://{tên repo}.onrender.com
# II.Sử dụng API 🛠
## 1. GET API
* Lấy dữ liệu nhiệt độ, độ ẩm, lượng nước, độ ẩm đất
```
#Python
import requests
import time
url = "https://{tên repo}.onrender.com/api/data/moitruong"
while True:
    headers = {
        "Content-Type": "application/json"
    }
    Get = requests.get(url)
    Data = Get.json()
    print(Data)
    time.sleep(1)
```
```
//JavaScript
const url = "https://{tên repo}.onrender.com/api/data/moitruong";
setInterval(async () => {
  try {
    const data = await (await fetch(url)).json();
    console.log(data);
  } catch (e) { console.error(e); }
}, 1000);
```
* Lấy dữ liệu giới hạn của nhiệt độ và độ ẩm 
```
#Python
import requests
import time
url = "https://{tên repo}.onrender.com/api/data/caidat"
while True:
    headers = {
        "Content-Type": "application/json"
    }
    Get = requests.get(url)
    Data = Get.json()
    print(Data)
    time.sleep(1)
```
```
//JavaScript
const url = "https://{tên repo}.onrender.com/api/data/caidat";
setInterval(async () => {
  try {
    const data = await (await fetch(url)).json();
    console.log(data);
  } catch (e) { console.error(e); }
}, 1000);
```
## 2. POST API
* Gửi dữ liệu môi trường lên API
```
#Python
import requests
import time
url = "https://api-moi-truong.onrender.com/api/data/moitruong"
while True:
    data = {
        "nhietdo": random.randint(20,40),
        "doam" : random.randint(20,40),
        "luongnuoc" : random.randint(20,40),
        "đoamat": random.randint(0, 1)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=data, headers=headers)
    print(response)
    time.sleep(1);
```
```
//JavaScript
const url = "https://api-moi-truong.onrender.com/api/data/moitruong";
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
setInterval(() => {
  const data = {
    nhietdo: randomInt(20, 40),
    doam: randomInt(20, 40),
    luongnuoc: randomInt(20, 40),
    đoamat: randomInt(0, 1)
  };
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => console.log("Status:", res.status))
  .catch(err => console.error("Lỗi:", err));
}, 1000);
```
* Gửi giới hạn môi trường lên API
```
#Python
import requests
import random
import time
url = "https://api-moi-truong.onrender.com/api/data/caidat"
while True:
    value = {
        "nhietdotoithieu" : random.randint(20,40),
        "nhietdotoida" : random.randint(20,40),
        "doamtoithieu" : random.randint(20,40),
        "doamtoida" : random.randint(20,40)
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=value, headers=headers)
    print(response)
    time.sleep(1);
```
```
//JavaScript
const url = "https://api-moi-truong.onrender.com/api/data/caidat";

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

setInterval(() => {
  const value = {
    nhietdotoithieu: randomInt(20, 40),
    nhietdotoida: randomInt(20, 40),
    doamtoithieu: randomInt(20, 40),
    doamtoida: randomInt(20, 40)
  };

  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(value)
  })
  .then(res => console.log("Status:", res.status))
  .catch(err => console.error("Lỗi:", err));
}, 1000);
```
# III. Lời kết 📝
* Cảm ơn bạn đã sử dụng dự án của mình đây là 1 dự án nhỏ trong 1 dự án khác về nông nghiệp của mình sắp tới mình sẽ đưa toàn bộ dự án lên github và rất mong được các bạn sử dụng, mình rất mong nhận được lời góp ý từ mọi người để phát triển dự án tốt hơn.
# IV. Thông tin liên hệ 📞
* Gmail: Kinerno2008@gmail.com
* Facebook: https://www.facebook.com/DucwsChinhs
