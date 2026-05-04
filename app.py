from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "return App is running v2"

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return "v1.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
