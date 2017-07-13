# -*- coding:utf-8 -*-
"""formDAO """
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def insert(params):
	"""This function inserts into the database the informations about a page created by user"""
	conn = mysql.connect()
	cursor = conn.cursor()
	insertion = """INSERT INTO `pages_web`(article,titre,chemin_image,taille_titre,numero_page,user_mail)
	 			VALUES(%(_article)s,%(_titre)s,%(_chemin_image)s,%(_taille_titre)s,%(_numero_page)s,%(_user_mail)s)"""
	cursor.execute(insertion, params)
	conn.commit()
	cursor.close()


def isPageExist(params):
	"""This function cheks if the page number of apage exist in the database for a specifical user"""
	conn = mysql.connect()
	cursor = conn.cursor()
	query = """SELECT `numero_page` FROM `pages_web` WHERE user_mail = %(_user_mail)s and numero_page=%(_numero_page)s"""
	cursor.execute(query, params)
	conn.commit()
	val_query = cursor.fetchone()
	cursor.close()
	return val_query


def update(params):
	"""This function updates in the database the informations about a page created by user"""
	conn = mysql.connect()
	cursor = conn.cursor()
	update_database = """UPDATE `pages_web`
					SET article=%(_article)s, titre=%(_titre)s, chemin_image=%(_chemin_image)s, taille_titre=%(_taille_titre)s, numero_page=%(_numero_page)s, user_mail=%(_user_mail)s 
					WHERE user_mail=%(_user_mail)s and numero_page=%(_numero_page)s"""
	cursor.execute(update_database, params)
	conn.commit()
	cursor.close()

def checkPage(params):
	"""This function returns the informations of a user page"""
	conn = mysql.connect()
	cursor = conn.cursor()
	query = """SELECT 'article',`titre`,'chemin_image','taille_titre',`numero_page`,`user_mail` FROM `pages_web`"""
	cursor.execute(query, params)
	conn.commit()
	val_query = cursor.fetchone()
	cursor.close()
	return val_query
