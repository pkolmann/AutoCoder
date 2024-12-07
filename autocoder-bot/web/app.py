from flask import Flask, jsonify
import random
app = Flask(__name__)

users = [
    {'Firstname': 'John', 'Lastname': 'Doe', 'UserId': '123', 'year of birth': 1990, 'email address': 'john.doe@example.com'},
    {'Firstname': 'Jane', 'Lastname': 'Smith', 'UserId': '456', 'year of birth': 1985, 'email address': 'jane.smith@example.com'},
    {'Firstname': 'Alice', 'Lastname': 'Johnson', 'UserId': '789', 'year of birth': 1995, 'email address': 'alice.johnson@example.com'}
]

@app.route('/users')
def get_users():
    return jsonify(users=random.choices(users, k=random.randint(3, 10)))

if __name__ == '__main__':
    app.run()
