# -*- coding:utf-8 -*-
from flask import Flask,request,flash
from flaskext.mysql import MySQL
import sys
	
mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
def get(username,pagenumber):
	"""Cette fonction va récuperer les titres, taille de titre, article et image et les afficher"""
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * from pages_web where user_mail='" + username + "' and numero_page='" + pagenumber + "'")
	data = cursor.fetchall()
	page = {}
	page["article"]="Pas d article"
	page["titre"]="Pas de titre"
	page["chemin_image"]=""
	page["taille"]="1"

	if data is None:
		return None
	else:
		for row in data:
			page["article"]=row[0]
			page["titre"]=row[1]
			page["chemin_image"]=row[2]
			page["taille"]=row[3]
	return (page)