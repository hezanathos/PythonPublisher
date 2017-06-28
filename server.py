# -*- coding:utf-8 -*-

from flask import Flask,request
from flask import flash,make_response,session
from flask import render_template

app = Flask('Dynamique')
app.secret_key = 'cle'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # la session dure une heure

@app.route('/',methods=['GET', 'POST'])
def Accueil() :
	return render_template('Accueil.html')

@app.route('/connexion', methods=['GET', 'POST'])
def Connexion():
	if request.method == 'POST':
		mail=request.form['mail']
		session['pseudo'] =mail
		return render_template('connexion.html')
	return render_template('Accueil.html',Nom=mail) #Liste des pages créées

app.run(debug=True)