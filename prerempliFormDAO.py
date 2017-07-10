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
def get(params):
	"""Cette fonction va récuperer les titres, taille de titre, article et image et les afficher"""
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT 'article',`titre`,'chemin_image','taille_titre',`numero_page`,`user_mail` from pages_web where article=%(_article)s, titre=%(_titre)s, chemin_image=%(_chemin_image)s, taille_titre=%(_taille_titre)s, numero_page=%(_numero_page)s, user_mail=%(_user_mail)s")

	data = cursor.fetchall()
	page = {}
	page["article"]="Veuillez créer votre article"
	page["titre"]="Veuillez ajouter une image"
	page["chemin_image"]="aucune.jpg"
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