from flask import Flask, jsonify, request
from flask_cors import CORS
import random

class Leaderboard:
    def __init__(self):
        self.winning_bets = []

    def add_winning_bet(self, bet_amount):
        
        self.winning_bets.append(bet_amount)
        self.winning_bets = sorted(self.winning_bets, reverse=True)[:10]

    def get_leaderboard(self):
        return self.winning_bets