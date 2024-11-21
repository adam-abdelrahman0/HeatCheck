import base64
from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)

# Enable CORS for all routes (allowing Angular frontend to interact with Flask backend)
CORS(app)

# Example leaderboard data (can be replaced with actual database or dynamic data)
leaderboard_data = [
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90}
]

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Endpoint to fetch leaderboard data"""
    return jsonify(leaderboard_data)

@app.route('/submit-score', methods=['POST'])
def submit_score():
    """Endpoint to submit a new outfit score"""
    data = request.get_json()  # Get JSON data sent from frontend

    # Example: Process the incoming data (validate, save to database, etc.)
    print("Received outfit data:", data)
    
    # For now, we'll just simulate a successful submission
    response = {"message": "Score submitted successfully!", "data": data}
    return jsonify(response)

@app.route('/process-image', methods=['POST'])
def process_image():
    """Endpoint to process an image from the webcam."""
    data = request.get_json()
    image_data = data.get('image')  # Expecting a base64-encoded image string

    if not image_data:
        return jsonify({"error": "No image provided."}), 400

    # Decode the base64 image
    try:
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception as e:
        return jsonify({"error": f"Error decoding image: {e}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
