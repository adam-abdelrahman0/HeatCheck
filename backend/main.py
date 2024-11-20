from flask import Flask, jsonify, request
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(debug=True)