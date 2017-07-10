# -*- coding:utf-8 -*-
from flask import Flask, request, flash, session
from flaskext.mysql import MySQL
import sys

mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def liste_auteurs():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("""SELECT `user_mail`,`titre`,`numero_page` FROM `pages_web`""")
	data = cursor.fetchall()

	liste_finale=[]
	for row in data:
		user_mail = row[0]
		titre = row[1]
		numero_page = row[2]
		flag = False
		listeTMP = [None,None,None,None]
		for idx,sublist in enumerate(liste_finale):
			if user_mail in sublist:
				sublist[int(numero_page)] = titre
				liste_finale[idx] = sublist
				flag = True

		if not flag:		
			listeTMP[0] = user_mail
			listeTMP[int(numero_page)] = titre
			liste_finale.append(listeTMP)
	cursor.close()
	return (liste_finale)

def liste_Pages():
	if 'pseudo' in session:
		conn = mysql.connect()
		cursor = conn.cursor()
		user_mail=session.get('pseudo')
		cursor.execute("SELECT `numero_page` FROM `pages_web` WHERE user_mail ='"+ user_mail + "'")
		data = cursor.fetchall()

		liste_finale = []
		for row in data:
			listeTMP = row[0]
			liste_finale.append(listeTMP)

		cursor.close()
		return (liste_finale)
	else:
		return False