from flask import Flask, render_template, request, redirect, url_for
from db import *


mycursor.execute("CREATE DATABASE IF NOT EXISTS biltreff")
mycursor.execute("USE biltreff")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS vehicle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL
    
);       
                 
""")


mycursor.execute("""
CREATE TABLE IF NOT EXISTS contact_form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id) ON DELETE CASCADE
);

""")



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f"Name: {name}, Email: {email}, Message: {message}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
