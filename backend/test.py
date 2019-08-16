from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'FrankieandSue'
app.config['MYSQL_DB'] = 'tvshow-catalog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# Init MySQL
mysql = MySQL(app)

@app.route('/')
def index():

    # Create cursor
    cur = mysql.connection.cursor()

    cur.execute("SELECT username FROM user");

    data = cur.fetchall()
    return jsonify(data)