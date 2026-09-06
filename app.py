from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8839750399:AAEYXRzgs9lAqpGXkbFrhVCwaTiprIuuC38"
CHAT_ID = "1838683997"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    msg = f"Есть захождение"
    send_telegram(msg)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
