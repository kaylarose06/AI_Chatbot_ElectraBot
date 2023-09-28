from flask import Flask, render_template, url_for, jsonify, request, session, redirect
from chat import get_response
from flask_cors import CORS
from passlib.hash import sha256_crypt
import psycopg2

app = Flask("__main__")
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/signup")
def signup():
    return render_template("login.html")

@app.get("/chat")
def chat():
    return render_template("chat.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response }
    return jsonify(message)


# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres1234',
    'host': 'localhost',
    'port': '5432'
}

# Function to encrypt passwords using SHA-256
def encrypt_password(password):
    return sha256_crypt.encrypt(password)

# API endpoint for user registration
@app.post("/apiRegisterUser")
def register_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    encrypted_password = encrypt_password(password)

    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Insert user data into the database
        cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                       (name, email, encrypted_password))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to verify the encrypted password
def verify_password(password, hashed_password):
    return sha256_crypt.verify(password, hashed_password)

# API endpoint for user login
@app.post("/apiLoginUser")
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Retrieve the user data from the database using the email
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user_data = cursor.fetchone()

        if user_data:
            _, _, _, hashed_password = user_data
            if verify_password(password, hashed_password):
                # Passwords match, login successful
                cursor.close()
                conn.close()
                return jsonify({'message': 'Login successful'}), 200
            else:
                # Passwords do not match, login failed
                cursor.close()
                conn.close()
                return jsonify({'error': 'Invalid credentials'}), 401
        else:
            # User with the given email not found, login failed
            cursor.close()
            conn.close()
            return jsonify({'error': 'Invalid credentials'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Add more endpoints as needed.
if __name__ == '__main__':
    app.run(debug=True)