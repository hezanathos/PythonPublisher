# -*- coding:utf-8 -*-
"""inscriptionDAO"""
from flask import Flask
from flaskext.mysql import MySQL
from pymysql.err import IntegrityError


mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def inscription(params):
	"""This function register a new user"""
	conn = mysql.connect()
	cursor = conn.cursor()
	query = """INSERT INTO `inscription`(username,mdp,mail) VALUES(%(_pseudo)s,%(_mdp)s,%(_mail)s)"""
	try:
		cursor.execute(query, params)
		conn.commit()

	except IntegrityError:
		conn.rollback()
		return False

	cursor.close()
	return True
