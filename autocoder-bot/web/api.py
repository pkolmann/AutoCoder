from flask import Flask, jsonify
app = Flask(__name__)

users = [
    {"Firstname": "John", "Lastname": "Doe", "UserId": 1, "year of birth": 1990, "email address": "john.doe@example.com"},
    {"Firstname": "Jane", "Lastname": "Smith", "UserId": 2, "year of birth": 1985, "email address": "jane.smith@example.com"},
    {"Firstname": "Michael", "Lastname": "Johnson", "UserId": 3, "year of birth": 1995, "email address": "michael.johnson@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run()
