#############################################################
#11.12.2023 #BlackHat
#############################################################

from flask import Flask, render_template, request
import mysql.connector
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

# MySQL Database Configuration
db_config = {
    'host': 'YOUR_DB_HOST',
    'user': 'YOUR_DB_USER',
    'password': 'YOUR_DB_PASSWORD',
    'database': 'YOUR_DB_NAME',
}

# Function to create a connection and cursor
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
    except Exception as e:
        print(e)

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        connection = create_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO anmeldungen (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
            connection.commit()
            print("Data inserted successfully")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

        return render_template('success.html')

    return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True, port=8000)
