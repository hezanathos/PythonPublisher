# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import flash,make_response,session,redirect,url_for
from flask import render_template

import sys
import connexionDAO


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
	var=session.get('pseudo')
	if var==None:
		return render_template('Accueil.html',pseudo="")
	return render_template('Accueil.html',pseudo=session['pseudo'])

@app.route('/connexion', methods=['GET','POST'])
def Connexion():
	if request.method == 'POST':
		mail=request.form['mail']
		mdp=request.form['mdp']
		if connexionDAO.check(mail,mdp):
			session['pseudo'] =mail
			return redirect(url_for('Accueil'))
		else:
			flash('Mauvais mot de passe')
	return render_template('connexion.html')
	
@app.route('/inscription',methods=['GET','POST'])
def Inscriptions():
	if request.method == 'POST':
		pseudo=request.form['pseudo']
		mail=request.form['mail']
		mdp=request.form['mdp']
		confirmer_mdp=request.form['confirmer_mdp']
		if mdp == confirmer_mdp:
			print('true',file=sys.stderr)
			return redirect('/connexion')

		else:
			flash("Veuillez saisir un mot de passe identique")
			return render_template('inscription.html')
	else:
		return render_template('inscription.html')


@app.route('/deconnexion')
def Logout():
	session.pop('pseudo', None)
	flash('Deconnexion reussie')
	return render_template('Accueil.html')

app.run(debug=True)