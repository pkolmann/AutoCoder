from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/users')
    def get_users():
        users = [
            {"Firstname": "John", "Lastname": "Doe", "UserId": 1, "year of birth": 1990, "email address": "john.doe@example.com"},
            {"Firstname": "Jane", "Lastname": "Smith", "UserId": 2, "year of birth": 1985, "email address": "jane.smith@example.com"},
            {"Firstname": "Alice", "Lastname": "Johnson", "UserId": 3, "year of birth": 1995, "email address": "alice.johnson@example.com"}
        ]
        return jsonify(users)

    return app
