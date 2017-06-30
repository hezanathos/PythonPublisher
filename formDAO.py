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
	insertion="""INSERT INTO pages_web VALUES( %(_article)s, %(_titre)s, %(_chemin_image)s, %(_taille_titre)s, %(_numero_page)s, %(_user_mail)s )"""
	#(article, titre, chemin_image, taille_titre, numero_page, user_mail)
	try:
		cursor.execute(insertion,params)
		conn.commit()

	except IntegrityError as e:
		return False

	cursor.close()

	return True
	 