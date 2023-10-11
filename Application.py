# Import flask and datetime module for showing date and time
import datetime
import sqlite3
from sqlite3 import Error
from flask import Flask

 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
 
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
#get each message, get all the data
     
# Running app




def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
@app.route("/get_messages/<clientID>")
def getMessages(clientID):

    return json()

if __name__ == '__main__':
    app.run(debug=True)
    create_connection("data.db")
    createTables()

    "CREATE TABLE User(userID int primary key, name TEXT, username TEXT);"
    "CREATE TABLE TherapistUser(therapistuserID int primary key references User(userID));"
    "CREATE TABLE ClientUser(userID int primary key foreign key references User(userID), TherapistUserID foreign key references TherapistUser(TherapistUserID));"



