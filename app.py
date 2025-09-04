from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json  # Get JSON data from the frontend
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    # Save the user to the database
    new_subscriber = Subscriber(name=name, email=email)
    db.session.add(new_subscriber)
    db.session.commit()

    return jsonify({"message": f"Thanks for signing up, {name}!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
