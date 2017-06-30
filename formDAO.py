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

def formulaire(params):
	conn = mysql.connect()
	cursor = conn.cursor()
	query="""INSERT INTO pages_web VALUES( %(_numero_page)s, %(_titre)s, %(_taille_titre)s, %(_chemin_image)s, %(_article)s, %(_user_mail)s )"""
	try:
		cursor.execute(query,params)
		conn.commit()

	except IntegrityError as e:
		return False

	cursor.close()

	return True
	 