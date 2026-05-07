from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running from ArgoCD GitOps."

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return os.getenv("APP_MODE", "default")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
