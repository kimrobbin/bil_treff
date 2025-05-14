from flask import Flask, render_template, request, redirect, url_for
from db import *

 # Makes the database
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
    vehicle_id INT NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(id) ON DELETE CASCADE

);

""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS aktiviteter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP


);

""")


app = Flask(__name__)


@app.route('/')
def index():
    # Henter alle deltakere
    mycursor.execute("""
        SELECT contact_form.name, contact_form.email, vehicle.type, vehicle.brand, contact_form.date
        FROM contact_form
        JOIN vehicle ON contact_form.vehicle_id = vehicle.id
    """)
    deltagere = mycursor.fetchall()
    
    # Henter alle aktiviteter
    mycursor.execute("SELECT * FROM aktiviteter")
    aktiviteter = mycursor.fetchall()
    
    # senderer til index.html
    return render_template("index.html", deltagere=deltagere, aktiviteter=aktiviteter)

def get_activities():
   
    return render_template("index.html", ) 

# Regristreing logik
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    vehicle = request.form.get('vehicle')
    merke = request.form.get('type_vehicle')

    # print(f"Name: {name}, Email: {email}, Vehicle: {vehicle}, Brand: {merke}")

    # Insert into the vehicle table
    sql_statement2 = "INSERT INTO vehicle (type, brand) VALUES (%s, %s)"
    values2 = (vehicle, merke)
    mycursor.execute(sql_statement2, values2)

    # Get the ID of the newly inserted vehicle
    vehicle_id = mycursor.lastrowid

    # Insert into the contact_form table with the vehicle_id
    sql_statement = "INSERT INTO contact_form (name, email, vehicle_id) VALUES (%s, %s, %s)"
    values = (name, email, vehicle_id)
    mycursor.execute(sql_statement, values)

    dbconn.commit()

    return redirect(url_for('index'))

<<<<<<< Updated upstream

# Aktivitet logik

@app.route('/aktivitet', methods=['POST'])
def submit_activity():
    name = request.form.get('submit_aktivitet')

    if name:
        sql_statement = "INSERT INTO aktiviteter (name) VALUES (%s)"
        mycursor.execute(sql_statement, (name,))
        dbconn.commit()

=======
@app.route("/deltagere", methods=["POST"])
def deltagere():
    mycursor.execute("SELECT * FROM contact_form")
    deltagere = mycursor.fetchall()
    return render_template("index.html", deltagere=deltagere)
>>>>>>> Stashed changes
   
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
