# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import flash,make_response,session,redirect,url_for
from flask import render_template
from inscriptionDAO import *
from formDAO import *
from pageDAO import *

import sys
import os
import connexionDAO
import pageDAO
import articleDAO



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
	user_mail=session.get('pseudo')
	if user_mail==None:
		return render_template('Accueil.html',pseudo="",title=title,liste=articleDAO.liste_auteurs())
	return render_template('Accueil.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())

@app.route('/connexion', methods=['GET','POST'])
def Connexion():
	title="Connexion"
	user_mail=session.get('pseudo')
	if request.method == 'POST':
		mail=request.form['mail']
		mdp=request.form['mdp']
		if connexionDAO.check(mail,mdp):
			session['pseudo'] =mail
			return redirect('/')
		else:
			flash('Mauvais mot de passe')
	return render_template('connexion.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
	
@app.route('/inscription',methods=['GET','POST'])
def Inscriptions():
	user_name=session.get('pseudo')
	title="Inscription"
	if request.method == 'POST':
		params = {
		'_pseudo' : request.form['pseudo'],
		'_mail' : request.form['mail'],
		'_mdp' : request.form['mdp'],
		'_confirmer_mdp' : request.form['confirmer_mdp']
		}
		if request.form['mdp'] == request.form['confirmer_mdp']:
			if inscription(params):
				return redirect('/connexion')
			else:
				flash("Cette adresse mail existe déjà")
				return redirect('inscription.html')
		else:
			flash("Veuillez saisir un mot de passe identique")
			return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
	else:
		return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())


@app.route('/formulaire',methods=['GET','POST'])
def Formulaire():
	user_mail=session.get('pseudo')
	title= "Formulaire"
	if request.method == 'POST':
		params = {
		'_numero_page' : request.form['numero_page'],
		'_titre' : request.form['titre'],
		'_taille_titre' : request.form['taille_titre'],
		'_chemin_image' : request.form['chemin_image'],
		'_article' : request.form['article'],
		'_user_mail' : user_mail
		}

		select_num_page = insertOrUpdate(params)
		if select_num_page is not None:


		result_requete = insertOrUpdate(params)
		if result_requete is not None:
			update(params)
			flash('Formulaire mis à jour')
			return redirect('/')
		else:
			insert(params)
			flash('Formulaire complet')
			return redirect('/')
	else:
		return render_template('formulaire.html',pseudo=user_mail, title=title,liste=articleDAO.liste_auteurs())

@app.route('/pages',methods=['GET','POST'])
def Pages():
	title="Nos Publishers"
	user_mail=session.get('pseudo')
	return render_template('pages.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())

@app.route('/pages/<username>/<pagenumber>',methods=['GET','POST'])
def Creations(username,pagenumber):
	page=get(username,pagenumber)
	return render_template('page.html',page=page,titre=page["titre"])

	page=pageDAO.get(username,pagenumber)
	return render_template('page.html',page=page,titre=page["titre"],liste=articleDAO.liste_auteurs())


@app.route('/deconnexion')
def Logout():
	session.pop('pseudo', None)
	flash('Deconnexion reussie')
	return redirect('/')

@app.route('/liste')
def Liste():
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]

	return render_template('Accueil.html',liste=liste)


app.run(debug=True)