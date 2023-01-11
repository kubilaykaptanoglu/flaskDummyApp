from flask import Flask, request, jsonify
app = Flask(__name__)

class DataStore():
    status_code = "200"

data = DataStore()

@app.route("/")
def about():
    return "Kubilay Kaptanoğlu"

@app.route("/healthz")
def health():
    # if status_code == "":
    #     return jsonify({
    #         "status" : 200
    #     })
    # else:
    return jsonify({
        "status" : data.status_code
    }), data.status_code

@app.route("/change")
def change():
    args = request.args
    data.status_code = args.get('status_code')
    return f"You changed the status code to {data.status_code}"

if __name__ == "__main__":
    app.run()
