# -*- coding:utf-8 -*-
"""articleDAO"""
from flask import Flask, session
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask('Dynamique')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def liste_auteurs():
	""" This function returns a list that contains the name of authors of different pages"""
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("""SELECT `user_mail`,`titre`,`numero_page` FROM `pages_web`""")
	data = cursor.fetchall()
	liste_finale = []
	for row in data:
		user_mail = row[0]
		titre = row[1]
		numero_page = row[2]
		flag = False
		list_tmp = [None, None, None, None]
		for idx, sublist in enumerate(liste_finale):
			if user_mail in sublist:
				sublist[int(numero_page)] = titre
				liste_finale[idx] = sublist
				flag = True
		if not flag:
			list_tmp[0] = user_mail
			list_tmp[int(numero_page)] = titre
			liste_finale.append(list_tmp)

	cursor.close()
	return liste_finale

def liste_pages():
	""" This function returns a list that contains the number of page realized by an author"""
	if 'pseudo' in session:
		conn = mysql.connect()
		cursor = conn.cursor()
		user_mail = session.get('pseudo')
		cursor.execute("SELECT `numero_page` FROM `pages_web` WHERE user_mail ='"+ user_mail + "'")
		data = cursor.fetchall()
		liste_finale = []
		for row in data:
			list_tmp = row[0]
			liste_finale.append(list_tmp)

		cursor.close()
		return liste_finale

	return False
