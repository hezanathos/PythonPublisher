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

def liste_auteurs(params):
	conn = mysql.connect()
	cursor = conn.cursor()


	query = """SELECT `user_mail` and 'titre' FROM `pages_web` WHERE user_mail = %(_user_mail)s and titre=%(_titre)s"""
	liste=[]
	liste.append('user_mail')
	liste_two=[]
	for user_mail in liste
		liste_two.append(user_mail,titre)

	


	cursor.execute(query,params)
	conn.commit()
	val_query=cursor.fetchone()

	cursor.close()
		
	return (val_query)