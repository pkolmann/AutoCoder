from flask import Flask, jsonify
app = Flask(__name__)

users = [
    {'firstname': 'John', 'lastname': 'Doe', 'userid': '1234', 'year_of_birth': 1985, 'email': 'john.doe@example.com'},
    {'firstname': 'Jane', 'lastname': 'Smith', 'userid': '5678', 'year_of_birth': 1990, 'email': 'jane.smith@example.com'},
    {'firstname': 'Alice', 'lastname': 'Johnson', 'userid': '9012', 'year_of_birth': 1988, 'email': 'alice.johnson@example.com'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run()
