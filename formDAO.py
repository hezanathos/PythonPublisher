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

def formulaire(titre, taille_titre, chemin_image, article, var):
	data = {"titre":titre,"taille_titre":taille_titre, "chemin_image":chemin_image, "article":article, "var"}
	cursor = mysql.connect().cursor()
	cursor.execute("""INSERT INTO pages_web (titre, taille_titre, chemin_image, article) VALUES(%(titre)s, %(taille_titre)s, %(chemin_image)s, %(article)s )""",data)
	#data = cursor.fetchone()
	if data is None:
		print('data is none', file=sys.stderr)
		return False
	else:
		print('data is not none', file=sys.stderr)
		return True

