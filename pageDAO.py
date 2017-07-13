# -*- coding:utf-8 -*-
"""pageDAO"""
from flask import Flask
from flaskext.mysql import MySQL

	
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
	cursor.execute("SELECT * FROM pages_web WHERE user_mail='" + username + "' and numero_page='" + pagenumber + "'")
	data = cursor.fetchall()
	page = {}
	page["article"] = "Veuillez créer votre article"
	page["titre"] = "Veuillez ajouter une image"
	page["chemin_image"] = "aucune.jpg"
	page["taille"] = "1"

	if data is None:
		return None
	else:
		for row in data:
			page["article"] = row[0]
			page["titre"] = row[1]
			page["chemin_image"] = row[2]
			page["taille"] = row[3]

	return page
