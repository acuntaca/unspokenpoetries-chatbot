from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pesan = data["pesan"]

    balasan = chatbot(pesan)

    return jsonify({
        "balasan": balasan
    })

if __name__ == "__main__":
    app.run(debug=True)