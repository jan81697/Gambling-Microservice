from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from leaderboard import Leaderboard

app = Flask(__name__)
CORS(app)

tokens = 100 
leaderboard = Leaderboard() 

@app.route('/place_bet', methods=['POST'])
def place_bet():
    global tokens
    data = request.get_json()
    bet_amount = data.get('bet_amount', 0)

    # Validate bet amount
    if bet_amount <= 0:
        return jsonify({"message": "Invalid bet amount. Please enter a positive number.", "tokens": tokens})
    if bet_amount > tokens:
        return jsonify({"message": "Insufficient tokens. Please enter a lower bet amount.", "tokens": tokens})

    # Determine win/loss and update tokens
    if random.choice([True, False]):
        tokens += bet_amount
        result = "You win!"
        leaderboard.add_winning_bet(bet_amount)
    else:
        tokens -= bet_amount
        result = "You lose!"
    tokens = max(0, tokens)

    return jsonify({"message": result, "tokens": tokens})

@app.route('/leaderboard', methods=['GET'])
def leaderboard_page():
    leaderboard.add_winning_bet(50)
    leaderboard.add_winning_bet(200)
    leaderboard.add_winning_bet(500)
    return jsonify({"leaderboard": leaderboard.get_leaderboard()})


if __name__ == '__main__':
    app.run(port=5000)
