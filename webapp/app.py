from flask import Flask, render_template, request, jsonify
from rpsapi import fetchsign
import random

app = Flask(__name__)

SIGNS = ["rock", "paper", "scissors"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.content_type.startswith('application/json'):
        image_data = request.json.get('image')
        user_sign = fetchsign.process_image(image_data)
    elif request.content_type.startswith('multipart/form-data'):
        image_file = request.files.get('image')
        user_sign = fetchsign.process_image(image_file.read())
    else:
        return jsonify({'error': 'Unsupported Content-Type'}), 400

    if user_sign == "unknown":
        return jsonify({'error': 'Could not recognize your sign.'}), 400

    computer_sign = random.choice(SIGNS)
    if user_sign == computer_sign:
        result = "tie"
    elif (user_sign == "rock" and computer_sign == "scissors") or \
         (user_sign == "paper" and computer_sign == "rock") or \
         (user_sign == "scissors" and computer_sign == "paper"):
        result = "win"
    else:
        result = "lose"
    return jsonify({
        "user_sign": user_sign,
        "computer_sign": computer_sign,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')