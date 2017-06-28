# -*- coding:utf-8 -*-

from flask import Flask,request
from flaskext.mysql import MySQL
from flask import flash,make_response,session
from flask import render_template

app = Flask('Dynamique')
mysql = MySQL()
app.secret_key = 'cle'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # la session dure une heure

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testbase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/',methods=['GET', 'POST'])
def Accueil() :
	return render_template('Accueil.html')

@app.route('/connexion', methods=['GET', 'POST'])
def Connexion():
	#if request.method == 'POST':
		#Nom=request.form['msg']
		#session['pseudo'] =Nom
	return render_template('connexion.html')
	#return render_template('pages.html') #Liste des pages créées

app.run(debug=True)