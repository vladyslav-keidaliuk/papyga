import mysql
import mysql.connector

TOKEN = 'YOUR_TOKEN'

GROUP_ID = YOUR_CHAT_ID

def DB():
    mydb = mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="yourdatabase"
            )
    return  mydb
