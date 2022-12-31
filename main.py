from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def about():
    return "Kubilay Kaptanoğlu"
@app.route("/healthz")
def health():
    return "OK"

if __name__ == "__main__":
    app.run()