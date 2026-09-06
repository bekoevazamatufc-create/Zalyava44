from flask import Flask, request
import requests

app = Flask(name)

TOKEN = "8839750399:AAEYXRzgs9lAqpGXkbFrhVCwaTiprIuuC38"
CHAT_ID = "1838683997"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    
    msg = f"🚨 НОВЫЙ ЗАХОД, БЛЯ! 🚨\n\nIP: {ip}\nБраузер: {ua}"
    
    send_telegram(msg)
    
    return "<h1>Сайт на ремонте</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
