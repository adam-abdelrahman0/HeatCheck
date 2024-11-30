import base64
from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)

# Enable CORS for all routes (allowing Angular frontend to interact with Flask backend)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Example leaderboard data (can be replaced with actual database or dynamic data)
leaderboard_data = [
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90},
    {"username": "user4", "score": 900},
    {"username": "user5", "score": 1010},
    {"username": "user6", "score": -5},
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90},
    {"username": "user4", "score": 900},
    {"username": "user5", "score": 1010},
    {"username": "user6", "score": -5},
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90},
    {"username": "user4", "score": 900},
    {"username": "user5", "score": 1010},
    {"username": "user6", "score": -5},
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90},
    {"username": "user4", "score": 900},
    {"username": "user5", "score": 1010},
    {"username": "user6", "score": -5},
    {"username": "user1", "score": 100},
    {"username": "user2", "score": 95},
    {"username": "user3", "score": 90},
    {"username": "user4", "score": 900},
    {"username": "user5", "score": 1010},
    {"username": "user6", "score": -5}
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
    try:
        # Get the image data from the POST 
        data = request.get_json()
        image_data = data.get('image', None)

        if not image_data:
            # If no image data is provided, return a 400 error
            return jsonify({'error': 'No image data provided'}), 400

        # Process da image
        print("Received image data:", image_data)

        #result = process_with_detectron2(image_data)
        #ranking_score = get_ranking(image_data)

        result = "success"
        ranking_score = 5

        # Return the processed result and ranking score as JSON
        return jsonify({
            "message": "Image processed successfully!",
            "result": result,  # Add any actual result from Detectron2 or ranking model
            "ranking_score": ranking_score
        })

    except Exception as e:
        # Return a 500 error in case of any exception
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
