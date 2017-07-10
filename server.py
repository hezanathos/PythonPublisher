# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for
from flaskext.mysql import MySQL
from flask import flash, make_response, session, redirect, url_for, send_file
from flask import render_template
from werkzeug import secure_filename

import sys
import os
import connexionDAO
import articleDAO
import inscriptionDAO
import uploadImageDAO
import formDAO
import pageDAO
import compteDAO
import pprint


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
def Accueil():
	title = "Python Publisher"
	user_mail = session.get('pseudo')
	if user_mail == None:
		return render_template('Accueil.html', pseudo = "", title = title, liste = articleDAO.liste_auteurs())
	return render_template('Accueil.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())

@app.route('/connexion', methods = ['GET', 'POST'])
def Connexion():
	title="Connexion"
	user_mail = session.get('pseudo')
	if request.method == 'POST':
		mail = request.form['mail']
		mdp = request.form['mdp']
		if connexionDAO.check(mail, mdp):
			session['pseudo'] = mail
			return redirect('/')
		else:
			flash('Mauvais mot de passe')
	if articleDAO.liste_Pages() == False:
		return render_template('connexion.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
	else:
		return render_template('connexion.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())
	
@app.route('/inscription', methods = ['GET', 'POST'])
def Inscriptions():
	user_mail = session.get('pseudo')
	title = "Inscription"
	if request.method == 'POST':
		params = {
		'_pseudo' : request.form['pseudo'],
		'_mail' : request.form['mail'],
		'_mdp' : request.form['mdp'],
		'_confirmer_mdp' : request.form['confirmer_mdp']
		}
		if request.form['mdp'] == request.form['confirmer_mdp']:
			if inscriptionDAO.inscription(params):
				return redirect('/connexion')
			else:
				flash("Cette adresse mail existe déjà")
				return redirect('/inscription')
		else:
			flash("Veuillez saisir un mot de passe identique")
			return redirect('/inscription')
	else:
		if articleDAO.liste_Pages() == False:
			return render_template('inscription.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
		else:
			return render_template('inscription.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())

def extension_ok(nomfic):
	""" Renvoie True si le fichier possède une extension d'image valide. """
	return '.' in nomfic and nomfic.rsplit('.', 1)[1] in ('png', 'jpg', 'jpeg', 'gif', 'bmp')


@app.route('/formulaire',methods=['GET','POST'])
def Formulaire():
	user_mail=session.get('pseudo')
	title= "Créer Page"
	if request.method == 'POST':
		f = request.files['chemin_image']
		params = {
		'_numero_page' : request.form['numero_page'],
		'_titre' : request.form['titre'],
		'_taille_titre' : request.form['taille_titre'],
		'_chemin_image' : secure_filename(f.filename),
		'_article' : request.form['article'],
		'_user_mail' : user_mail
		}
		DOSSIER_UPS=uploadImageDAO.createDirectory()
		if f: # on vérifie qu'un fichier a bien été envoyé
			if extension_ok(f.filename): # on vérifie que son extension est valide
				nom = secure_filename(f.filename)
				f.save(DOSSIER_UPS + nom)

				select_num_page = formDAO.isPageExist(params)
				if select_num_page is not None:
						formDAO.update(params)
						flash('Formulaire mis à jour')
						return redirect('/')
				else:
					formDAO.insert(params)
					flash('Formulaire complet')
					return redirect('/')
		else:
			return render_template('formulaire.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
	else:
		if articleDAO.liste_Pages() == False:
			return render_template('formulaire.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
		else:
			return render_template('formulaire.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())

@app.route('/modifpage/',methods=['GET','POST'])
def ModifPage():
	user_mail=session.get('pseudo')
	title= "Modifier Page"
	session['page_number'] = pagenumber
	if request.method == 'POST':
		f = request.files['chemin_image']
		params = {
		'_numero_page' : page_number,
		'_titre' : request.form['titre'],
		'_taille_titre' : request.form['taille_titre'],
		'_chemin_image' : secure_filename(f.filename),
		'_article' : request.form['article'],
		'_user_mail' : user_mail
		}
		DOSSIER_UPS=uploadImageDAO.createDirectory()
		if f: # on vérifie qu'un fichier a bien été envoyé
			if extension_ok(f.filename): # on vérifie que son extension est valide
				nom = secure_filename(f.filename)
				f.save(DOSSIER_UPS + nom)
		else:
			return render_template('modifpage.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
	else:
		if articleDAO.liste_Pages() == False:
			return render_template('modifpage.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
		else:
			return render_template('modifpage.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())

@app.route('/pages', methods = ['GET', 'POST'])
def Pages():
	title = "Nos Publishers"
	user_mail = session.get('pseudo')
	if articleDAO.liste_Pages() == False:
		return render_template('pages.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
	else:
		return render_template('pages.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())
 
@app.route('/pages/<username>/<pagenumber>',methods=['GET','POST'])
def Creations(username,pagenumber):	
	page = pageDAO.get(username,pagenumber)
	user_mail = session.get('pseudo')
	session['page_number'] = pagenumber
	chemin_image ="/static/"+username+"/"+page["chemin_image"]
	if articleDAO.liste_Pages() == False:
		return render_template('page.html', page = page, titre = page["titre"], pseudo = user_mail, liste = articleDAO.liste_auteurs(), chemin_image = chemin_image, page_number = pagenumber)
	else:
		return render_template('page.html', page = page, titre = page["titre"], pseudo = user_mail, liste = articleDAO.liste_auteurs(), chemin_image = chemin_image, page_number = pagenumber, listePages = articleDAO.liste_Pages())

@app.route('/deconnexion')
def Logout():
	session.pop('pseudo', None)
	flash('Deconnexion reussie')
	return redirect('/')

@app.route('/compte', methods = ['GET', 'POST'])
def Compte():
	title = "Mon Compte"
	user_mail = session.get('pseudo')
	if request.method == 'POST':
		params = {
		'_mdp' : request.form['mdp'],
		'_confirmer_mdp' : request.form['confirmer_mdp'],
		'_mail' : user_mail
		}
		if request.form['mdp'] == request.form['confirmer_mdp']:
			if compteDAO.update_compte(params):
				flash('Mot de passe changé')
				return redirect('/')
			else:
				flash('Mot de passe invalide')
				return redirect('/compte')
		else:
			flash("Veuillez saisir un mot de passe identique")
			return redirect('/compte')
	else:
		if articleDAO.liste_Pages() == False:
			return render_template('compte.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs())
		else:
			return render_template('compte.html', pseudo = user_mail, title = title, liste = articleDAO.liste_auteurs(), listePages = articleDAO.liste_Pages())

app.run(debug = True)