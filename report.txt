************* Module server
C:  3, 0: Exactly one space required after comma
from flask import Flask,request,redirect,url_for
                       ^ (bad-whitespace)
C:  3, 0: Exactly one space required after comma
from flask import Flask,request,redirect,url_for
                               ^ (bad-whitespace)
C:  3, 0: Exactly one space required after comma
from flask import Flask,request,redirect,url_for
                                        ^ (bad-whitespace)
C:  5, 0: Exactly one space required after comma
from flask import flash,make_response,session,redirect,url_for
                       ^ (bad-whitespace)
C:  5, 0: Exactly one space required after comma
from flask import flash,make_response,session,redirect,url_for
                                     ^ (bad-whitespace)
C:  5, 0: Exactly one space required after comma
from flask import flash,make_response,session,redirect,url_for
                                             ^ (bad-whitespace)
C:  5, 0: Exactly one space required after comma
from flask import flash,make_response,session,redirect,url_for
                                                      ^ (bad-whitespace)
C: 29, 0: Exactly one space required after comma
@app.route('/',methods=['GET', 'POST'])
              ^ (bad-whitespace)
C: 30, 0: No space allowed before :
def Accueil() :
              ^ (bad-whitespace)
W: 31, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 31, 0: Exactly one space required around assignment
	title="Python Publisher"
      ^ (bad-whitespace)
W: 32, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 32, 0: Exactly one space required around assignment
	user_mail=session.get('pseudo')
          ^ (bad-whitespace)
W: 33, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 33, 0: Exactly one space required around comparison
	if user_mail==None:
             ^^ (bad-whitespace)
W: 34, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 34, 0: Exactly one space required after comma
		return render_template('Accueil.html',pseudo="",title=title,liste=articleDAO.liste_auteurs())
                                       ^ (bad-whitespace)
C: 34, 0: Exactly one space required after comma
		return render_template('Accueil.html',pseudo="",title=title,liste=articleDAO.liste_auteurs())
                                                 ^ (bad-whitespace)
C: 34, 0: Exactly one space required after comma
		return render_template('Accueil.html',pseudo="",title=title,liste=articleDAO.liste_auteurs())
                                                             ^ (bad-whitespace)
C: 35, 0: Line too long (101/100) (line-too-long)
W: 35, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 35, 0: Exactly one space required after comma
	return render_template('Accueil.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                      ^ (bad-whitespace)
C: 35, 0: Exactly one space required after comma
	return render_template('Accueil.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                       ^ (bad-whitespace)
C: 35, 0: Exactly one space required after comma
	return render_template('Accueil.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                                   ^ (bad-whitespace)
C: 37, 0: Exactly one space required after comma
@app.route('/connexion', methods=['GET','POST'])
                                       ^ (bad-whitespace)
W: 39, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 39, 0: Exactly one space required around assignment
	title="Connexion"
      ^ (bad-whitespace)
W: 40, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 40, 0: Exactly one space required around assignment
	user_mail=session.get('pseudo')
          ^ (bad-whitespace)
W: 41, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 42, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 42, 0: Exactly one space required around assignment
		mail=request.form['mail']
      ^ (bad-whitespace)
W: 43, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 43, 0: Exactly one space required around assignment
		mdp=request.form['mdp']
     ^ (bad-whitespace)
W: 44, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 44, 0: Exactly one space required after comma
		if connexionDAO.check(mail,mdp):
                            ^ (bad-whitespace)
W: 45, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 45, 0: Exactly one space required after assignment
			session['pseudo'] =mail
                     ^ (bad-whitespace)
W: 46, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 47, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 48, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 49, 0: Line too long (103/100) (line-too-long)
W: 49, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 49, 0: Exactly one space required after comma
	return render_template('connexion.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                        ^ (bad-whitespace)
C: 49, 0: Exactly one space required after comma
	return render_template('connexion.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                         ^ (bad-whitespace)
C: 49, 0: Exactly one space required after comma
	return render_template('connexion.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                                     ^ (bad-whitespace)
C: 50, 0: Trailing whitespace (trailing-whitespace)
C: 51, 0: Exactly one space required after comma
@app.route('/inscription',methods=['GET','POST'])
                         ^ (bad-whitespace)
C: 51, 0: Exactly one space required after comma
@app.route('/inscription',methods=['GET','POST'])
                                        ^ (bad-whitespace)
W: 53, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 53, 0: Exactly one space required around assignment
	user_name=session.get('pseudo')
          ^ (bad-whitespace)
W: 54, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 54, 0: Exactly one space required around assignment
	title="Inscription"
      ^ (bad-whitespace)
W: 55, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 56, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 57, 0: Wrong hanging indentation (add 18 spaces).
		'_pseudo' : request.form['pseudo'],
  ^                 | (bad-continuation)
C: 58, 0: Wrong hanging indentation (add 18 spaces).
		'_mail' : request.form['mail'],
  ^                 | (bad-continuation)
C: 59, 0: Wrong hanging indentation (add 18 spaces).
		'_mdp' : request.form['mdp'],
  ^                 | (bad-continuation)
C: 60, 0: Wrong hanging indentation (add 18 spaces).
		'_confirmer_mdp' : request.form['confirmer_mdp']
  ^                 | (bad-continuation)
C: 61, 0: Wrong hanging indentation.
		}
  ^             |   | (bad-continuation)
W: 62, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 63, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 64, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 65, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 66, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 67, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 68, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 69, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 70, 0: Line too long (107/100) (line-too-long)
W: 70, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 70, 0: Exactly one space required after comma
			return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                            ^ (bad-whitespace)
C: 70, 0: Exactly one space required after comma
			return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                                             ^ (bad-whitespace)
C: 70, 0: Exactly one space required after comma
			return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                                                         ^ (bad-whitespace)
W: 71, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 72, 0: Line too long (106/100) (line-too-long)
W: 72, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 72, 0: Exactly one space required after comma
		return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                           ^ (bad-whitespace)
C: 72, 0: Exactly one space required after comma
		return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                                            ^ (bad-whitespace)
C: 72, 0: Exactly one space required after comma
		return render_template('inscription.html',pseudo=user_name,title=title,liste=articleDAO.liste_auteurs())
                                                                        ^ (bad-whitespace)
C: 75, 0: Exactly one space required after comma
@app.route('/formulaire',methods=['GET','POST'])
                        ^ (bad-whitespace)
C: 75, 0: Exactly one space required after comma
@app.route('/formulaire',methods=['GET','POST'])
                                       ^ (bad-whitespace)
W: 77, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 77, 0: Exactly one space required around assignment
	user_mail=session.get('pseudo')
          ^ (bad-whitespace)
W: 78, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 78, 0: Exactly one space required before assignment
	title= "Formulaire"
      ^ (bad-whitespace)
W: 79, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 80, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C: 81, 0: Wrong hanging indentation (add 18 spaces).
		'_numero_page' : request.form['numero_page'],
  ^                 | (bad-continuation)
C: 82, 0: Wrong hanging indentation (add 18 spaces).
		'_titre' : request.form['titre'],
  ^                 | (bad-continuation)
C: 83, 0: Wrong hanging indentation (add 18 spaces).
		'_taille_titre' : request.form['taille_titre'],
  ^                 | (bad-continuation)
C: 84, 0: Wrong hanging indentation (add 18 spaces).
		'_chemin_image' : request.form['chemin_image'],
  ^                 | (bad-continuation)
C: 85, 0: Wrong hanging indentation (add 18 spaces).
		'_article' : request.form['article'],
  ^                 | (bad-continuation)
C: 86, 0: Wrong hanging indentation (add 18 spaces).
		'_user_mail' : user_mail
  ^                 | (bad-continuation)
C: 87, 0: Wrong hanging indentation.
		}
  ^             |   | (bad-continuation)
W: 90, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 91, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 92, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 93, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 94, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 95, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 96, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 97, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 98, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W: 99, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:100, 0: Line too long (106/100) (line-too-long)
W:100, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:100, 0: Exactly one space required after comma
		return render_template('formulaire.html',pseudo=user_mail, title=title,liste=articleDAO.liste_auteurs())
                                          ^ (bad-whitespace)
C:100, 0: Exactly one space required after comma
		return render_template('formulaire.html',pseudo=user_mail, title=title,liste=articleDAO.liste_auteurs())
                                                                        ^ (bad-whitespace)
C:102, 0: Exactly one space required after comma
@app.route('/pages',methods=['GET','POST'])
                   ^ (bad-whitespace)
C:102, 0: Exactly one space required after comma
@app.route('/pages',methods=['GET','POST'])
                                  ^ (bad-whitespace)
W:104, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:104, 0: Exactly one space required around assignment
	title="Nos Publishers"
      ^ (bad-whitespace)
W:105, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:105, 0: Exactly one space required around assignment
	user_mail=session.get('pseudo')
          ^ (bad-whitespace)
W:106, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:106, 0: Exactly one space required after comma
	return render_template('pages.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                    ^ (bad-whitespace)
C:106, 0: Exactly one space required after comma
	return render_template('pages.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                     ^ (bad-whitespace)
C:106, 0: Exactly one space required after comma
	return render_template('pages.html',pseudo=user_mail,title=title,liste=articleDAO.liste_auteurs())
                                                                 ^ (bad-whitespace)
C:108, 0: Exactly one space required after comma
@app.route('/pages/<username>/<pagenumber>',methods=['GET','POST'])
                                           ^ (bad-whitespace)
C:108, 0: Exactly one space required after comma
@app.route('/pages/<username>/<pagenumber>',methods=['GET','POST'])
                                                          ^ (bad-whitespace)
C:109, 0: Exactly one space required after comma
def Creations(username,pagenumber):
                      ^ (bad-whitespace)
W:110, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:110, 0: Exactly one space required around assignment
	page=pageDAO.get(username,pagenumber)
     ^ (bad-whitespace)
C:110, 0: Exactly one space required after comma
	page=pageDAO.get(username,pagenumber)
                          ^ (bad-whitespace)
W:111, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:111, 0: Exactly one space required after comma
	return render_template('page.html',page=page,titre=page["titre"],liste=articleDAO.liste_auteurs())
                                   ^ (bad-whitespace)
C:111, 0: Exactly one space required after comma
	return render_template('page.html',page=page,titre=page["titre"],liste=articleDAO.liste_auteurs())
                                             ^ (bad-whitespace)
C:111, 0: Exactly one space required after comma
	return render_template('page.html',page=page,titre=page["titre"],liste=articleDAO.liste_auteurs())
                                                                 ^ (bad-whitespace)
W:115, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W:116, 0: Found indentation with tabs instead of spaces (mixed-indentation)
W:117, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:121, 0: Line too long (148/100) (line-too-long)
W:121, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                    ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                             ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                   ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                            ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                     ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                          ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                                    ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                                                                   ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                                                                        ^ (bad-whitespace)
C:121, 0: Exactly one space required after comma
	liste = [["maxime.rasse@orange.com","Titre2",None],["alex.lecoq@orange.com","Titre1",None,"Titre3"],["yusuf.makanjuola@orange.com",None,None,None]]
                                                                                                                                             ^ (bad-whitespace)
W:123, 0: Found indentation with tabs instead of spaces (mixed-indentation)
C:123, 0: Exactly one space required after comma
	return render_template('Accueil.html',liste=liste)
                                      ^ (bad-whitespace)
C:126, 0: Final newline missing (missing-final-newline)
C:  1, 0: Missing module docstring (missing-docstring)
W:  5, 0: Reimport 'redirect' (imported line 3) (reimported)
W:  5, 0: Reimport 'url_for' (imported line 3) (reimported)
W:  7, 0: Wildcard import inscriptionDAO (wildcard-import)
W:  8, 0: Wildcard import formDAO (wildcard-import)
C: 18, 0: Invalid constant name "app" (invalid-name)
C: 19, 0: Invalid constant name "mysql" (invalid-name)
C: 30, 0: Invalid function name "Accueil" (invalid-name)
C: 30, 0: Missing function docstring (missing-docstring)
C: 33, 4: Comparison to None should be 'expr is None' (singleton-comparison)
C: 38, 0: Invalid function name "Connexion" (invalid-name)
C: 38, 0: Missing function docstring (missing-docstring)
C: 52, 0: Invalid function name "Inscriptions" (invalid-name)
C: 52, 0: Missing function docstring (missing-docstring)
R: 55, 1: Unnecessary "else" after "return" (no-else-return)
R: 62, 2: Unnecessary "else" after "return" (no-else-return)
R: 63, 3: Unnecessary "else" after "return" (no-else-return)
C: 76, 0: Invalid function name "Formulaire" (invalid-name)
C: 76, 0: Missing function docstring (missing-docstring)
R: 79, 1: Unnecessary "else" after "return" (no-else-return)
R: 91, 2: Unnecessary "else" after "return" (no-else-return)
C:103, 0: Invalid function name "Pages" (invalid-name)
C:103, 0: Missing function docstring (missing-docstring)
C:109, 0: Invalid function name "Creations" (invalid-name)
C:109, 0: Missing function docstring (missing-docstring)
C:114, 0: Invalid function name "Logout" (invalid-name)
C:114, 0: Missing function docstring (missing-docstring)
C:120, 0: Invalid function name "Liste" (invalid-name)
C:120, 0: Missing function docstring (missing-docstring)
W:  3, 0: Unused url_for imported from flask (unused-import)
W:  5, 0: Unused make_response imported from flask (unused-import)
W:  7, 0: Unused import sys from wildcard import (unused-wildcard-import)
W:  7, 0: Unused import IntegrityError from wildcard import (unused-wildcard-import)
W: 11, 0: Unused import os (unused-import)
C: 10, 0: standard import "import sys" should be placed before "from flask import Flask, request, redirect, url_for" (wrong-import-order)
C: 11, 0: standard import "import os" should be placed before "from flask import Flask, request, redirect, url_for" (wrong-import-order)
C:  5, 0: Imports from package flask are not grouped (ungrouped-imports)

----------------------------------------------------------------------
Your code has been rated at -13.16/10 (previous run: -13.16/10, +0.00)

