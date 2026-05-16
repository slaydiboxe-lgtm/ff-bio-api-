from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running"
    })

@app.route("/bio", methods=["GET"])
def bio():

    access_token = request.args.get("access")
    bio_text = request.args.get("bio")

    if not access_token:
        return jsonify({
            "error": "missing access token"
        })

    if not bio_text:
        return jsonify({
            "error": "missing bio"
        })

    # your protobuf + encryption logic here

    return jsonify({
        "success": True,
        "bio": bio_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
