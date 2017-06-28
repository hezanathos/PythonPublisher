# -*- coding:utf-8 -*-

from flask import Flask,request
from flaskext.mysql import MySQL
from flask import flash,make_response,session
from flask import render_template
#import connexionDAO

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

@app.route('/connexion', methods=['GET','POST'])
def Connexion():
	if request.method == 'POST':
		mail=request.form['mail']
		mdp=request.form['mdp']
		#if connexionDAO.check(mail,mdp):
		session['pseudo'] =mail
		session['logged_in']=True
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

	return render_template('inscription.html',pseudo=pseudo,mail=mail,mdp=mdp,confirmer_mdp=confirmer_mdp)

app.run(debug=True)