# -*- coding:utf-8 -*-
"""comteDAO"""
from flask import Flask
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def update_compte(params):
	"""This fuction updates the user password"""
	conn = mysql.connect()
	cursor = conn.cursor()
	insertion = """UPDATE `inscription` SET mdp = %(_mdp)s WHERE mail = %(_mail)s"""

	cursor.execute(insertion, params)
	conn.commit()
	cursor.close()

	return True
