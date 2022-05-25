from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def api():
    context = jsonify({"stats": "OK!"})
    return context

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
