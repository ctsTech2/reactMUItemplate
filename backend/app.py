import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    response_message = f"Echo: {user_message}"
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)
