import mysql
import mysql.connector

TOKEN = 'YOUR_TOKEN'

GROUP_ID = YOUR_CHAT_ID

def db_connection():
    db = mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="yourdatabase"
            )
    return  db
