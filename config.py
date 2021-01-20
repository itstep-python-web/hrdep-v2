from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'itstepteacher.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'itstepteacher'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwerty_1029384756'
app.config['MYSQL_DATABASE_DB'] = 'itstepteacher$hrdep_db'

mysql = MySQL()
mysql.init_app(app)
