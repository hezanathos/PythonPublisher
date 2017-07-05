# -*- coding:utf-8 -*-
from flask import Flask,request,flash
from flaskext.mysql import MySQL
import sys
from pymysql.err import IntegrityError

mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def inscription(params):
	conn = mysql.connect()
	cursor = conn.cursor()
	query = """INSERT INTO `inscription`(username,mdp,mail) VALUES(%(_pseudo)s,%(_mdp)s,%(_mail)s)"""
	try:
		cursor.execute(query,params)
		conn.commit()

	except IntegrityError as e:
		conn.rollback()
		return False

	cursor.close()
	return True
