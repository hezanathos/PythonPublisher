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
	#data = {"titre":titre,"taille_titre":taille_titre, "chemin_image":chemin_image, "article":article, "var"}
	conn = mysql.connect()
	cursor = conn.cursor()
	insertion="""INSERT INTO pages_web (article, titre, chemin_image, taille_titre, numero_page, user_mail) VALUES( %(article)s, %(titre)s, %(chemin_image)s, %(taille_titre)s, %(numero_page)s, %(user_mail)s )"""
	try:
		cursor.execute(insertion,params)
		conn.commit()

	except IntegrityError as e:
		return False

	cursor.close()

	return True
	 