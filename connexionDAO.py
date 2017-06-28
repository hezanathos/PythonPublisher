# -*- coding:utf-8 -*-

from flaskext.mysql import MySQL
mysql = MySQL()

def check(mail,mdp):
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
	data = cursor.fetchone()
	if data is None:
		return "Username or Password is wrong"
	else:
		return "Logged in successfully"

