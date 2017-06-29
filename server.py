# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import flash,make_response,session,redirect,url_for
from flask import render_template

import sys
import connexionDAO
import formDAO


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
	return render_template('Accueil.html',pseudo=var)

@app.route('/connexion', methods=['GET','POST'])
def Connexion():
	var=session.get('pseudo')
	if request.method == 'POST':
		mail=request.form['mail']
		mdp=request.form['mdp']
		if connexionDAO.check(mail,mdp):
			session['pseudo'] =mail
			return redirect('/')
		else:
			flash('Mauvais mot de passe')
	return render_template('connexion.html',pseudo=var)
	
@app.route('/inscription',methods=['GET','POST'])
def Inscriptions():
	var=session.get('pseudo')
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
			return render_template('inscription.html',pseudo=var)
	else:
		return render_template('inscription.html',pseudo=var)


@app.route('/deconnexion')
def Logout():
	session.pop('pseudo', None)
	flash('Deconnexion reussie')
	return redirect('/')

@app.route('/formulaire',methods=['GET','POST'])
def Formulaire():
	var=session.get('pseudo')
	if request.method == 'POST':
		titre=request.form['titre']
		taille_titre=request.form['taille']
		chemin_image=request.form['image']
		article=request.form['article']
		if formDAO.formulaire(titre, taille_titre, chemin_image, article):
			session['pseudo'] =mail
			flash('Formulaire complet')
			return ('OK')
			#return redirect('/')
		else:
			flash('Formulaire non complet')
			return ('Form not complete')
	else:
		return render_template('vide.html',pseudo=var)




@app.route('/pages',methods=['GET','POST'])
def Pages():
	var=session.get('pseudo')
	return render_template('pages.html',pseudo=var)

@app.route('/vide',methods=['GET','POST'])
def Vide():
	var=session.get('pseudo')
	return render_template('vide.html',pseudo=var)

app.run(debug=True)