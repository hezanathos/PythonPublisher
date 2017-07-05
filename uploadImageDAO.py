# -*- coding:utf-8 -*-

from flask import Flask, request, flash, redirect, url_for,render_template
from flask import send_file
from werkzeug import secure_filename
import os

DOSSIER_UPS = '/Applications/PythonPublisher/static'

def extension_ok(nomfic):
    """ Renvoie True si le fichier possède une extension d'image valide. """
    return '.' in nomfic and nomfic.rsplit('.', 1)[1] in ('png', 'jpg', 'jpeg', 'gif', 'bmp')

def test(_chemin_image):
	if extension_ok(_chemin_image.secure_filename):
		nom = secure_filename(_chemin_image.filname)
		_chemin_image.save(DOSSIER_UPS+nom)
		return True
	else:
			return False
	return True
