# -*- coding:utf-8 -*-

from flask import Flask,request
from flaskext.mysql import MySQL
from flask import flash,make_response,session
from flask import render_template
import DAO/connexionDAO

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
	if request.method == 'POST':
		mail=request.form['mail']
		if connexionDAO.check(mail,mdp):
			session['pseudo'] =mail
			return redirect("http://localhost:5000/")
		else:
	return render_template('connexion.html')		
	

app.run(debug=True)