# -*- coding:utf-8 -*-
from flask import Flask,request
from flaskext.mysql import MySQL
import sys
mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
def check(mail,mdp):
	
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * from inscription where mail='" + mail + "' and mdp='" + mdp + "'")
	data = cursor.fetchone()
	if data is None:
		print('data is none', file=sys.stderr)
		return False
	else:
		print('data is not none', file=sys.stderr)
	return True

