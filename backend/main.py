import base64
from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import numpy as np
from models import getHeat

app = Flask(__name__)

# Enable CORS for all routes (allowing Angular frontend to interact with Flask backend)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Example leaderboard data (can be replaced with actual database or dynamic data)
leaderboard_data = [
    # {"username": "Christian", "score": 10000},
]

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Endpoint to fetch leaderboard data"""
    return jsonify(leaderboard_data)

@app.route('/submit-score', methods=['POST'])
def submit_score():
    """Endpoint to submit a new outfit score"""
    data = request.get_json()  # Get JSON data sent from frontend
    # print(data)

    # run the recieved data through the image cutting and heatcheck model
    # print("Received outfit data:", data)
    heat = getHeat(data["image"])

    
    # For now, we'll just simulate a successful submission
    response = {"message": "Score submitted successfully! heat is " + str(heat), "data": heat}
    return jsonify(response)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Get the image data from the POST 
        data = request.get_json()
        image_data = data.get('image', None)
        username = data.get('username', None)

        if not image_data:
            # If no image data is provided, return a 400 error
            return jsonify({'error': 'No image data provided'}), 400

        # Process da image
        # print("Received image data:", image_data)

        ranking_score = getHeat(image_data)
        if(ranking_score == "no human"):
            raise Exception("no human in image")

        result = "success"


        if(username != ''):
            if(any(x["username"] == username for x in leaderboard_data)):
                leaderboard_data[[entry["username"] for entry in leaderboard_data].index(username)]["score"] = ranking_score
            else:
                leaderboard_data.append({"username": username, "score": ranking_score})
        else:
            print("no username, not adding to leaderboard")

        # Return the processed result and ranking score as JSON
        return jsonify({
            "message": "Image processed successfully!",
            "result": result,
            "ranking_score": ranking_score
        })

    except Exception as e:
        # Return a 500 error in case of any exception
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
