# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import flash,make_response,session,redirect,url_for
from flask import render_template

import sys
import os
import connexionDAO
from inscriptionDAO import *


app = Flask('Dynamique')
mysql = MySQL()
app.secret_key = 'cle'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # la session dure une heure

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'siteweb_python'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/',methods=['GET', 'POST'])
def Accueil() :
	title="Python Publisher"
	var=session.get('pseudo')
	if var==None:
		return render_template('Accueil.html',pseudo="",title=title)
	return render_template('Accueil.html',pseudo=var,title=title)

@app.route('/connexion', methods=['GET','POST'])
def Connexion():
	title="Connexion"
	var=session.get('pseudo')
	if request.method == 'POST':
		mail=request.form['mail']
		mdp=request.form['mdp']
		if connexionDAO.check(mail,mdp):
			session['pseudo'] =mail
			return redirect('/')
		else:
			flash('Mauvais mot de passe')
	return render_template('connexion.html',pseudo=var,title=title)
	
@app.route('/inscription',methods=['GET','POST'])
def Inscriptions():
	var=session.get('pseudo')
	title="Inscription"
	if request.method == 'POST':
		params = {
		'_pseudo' : request.form['pseudo'],
		'_mail' : request.form['mail'],
		'_mdp' : request.form['mdp'],
		'confirmer_mdp' : request.form['confirmer_mdp']
		}
		if request.form['mdp'] == request.form['confirmer_mdp']:
			print('True',file=sys.stderr)
			if inscription(params):
				return redirect('/connexion')
			else:
				flash("Cette adresse mail existe déjà")
				return render_template('inscription.html')
		else:
			flash("Veuillez saisir un mot de passe identique")
			return render_template('inscription.html',pseudo=var,title=title)
	else:
		return render_template('inscription.html',pseudo=var,title=title)


@app.route('/deconnexion')
def Logout():
	session.pop('pseudo', None)
	flash('Deconnexion reussie')
	return redirect('/')

@app.route('/pages',methods=['GET','POST'])
def Pages():
	title="Nos Publishers"
	var=session.get('pseudo')
	return render_template('pages.html',pseudo=var,title=title)

@app.route('/vide',methods=['GET','POST'])
def Vide():
	title="Formulaire"
	var=session.get('pseudo')
	return render_template('vide.html',pseudo=var,title=title)

app.run(debug=True)