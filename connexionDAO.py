# -*- coding:utf-8 -*-
"""connexionDAO"""
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
def check(mail, mdp):
	"""This fuctions checks the correct username and password in the database"""
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * from inscription where mail='" + mail + "' and mdp='" + mdp + "'")
	data = cursor.fetchone()
	if data is None:
		return False
	else:
		return True
