from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
clicks = 0


@app.route('/')
def index():
    return send_from_directory('.', 'game.html')

@app.route('/gurt.png')
def gurt():
    return send_from_directory('.', 'gurt.png')

@app.route('/click', methods=['POST'])
def click():
    global clicks
    clicks += 1
    return jsonify({"clicks": clicks})


@app.route('/clicks', methods=['GET'])
def get_clicks():
    return jsonify({"clicks": clicks})

