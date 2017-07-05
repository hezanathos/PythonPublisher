# -*- coding:utf-8 -*-

from flask import Flask, request, flash, redirect, url_for,render_template
from flask import send_file
from werkzeug import secure_filename
import os

def createDirectory():
	DOSSIER_UPS = '/Applications/PythonPublisher/static/'+session.get('pseudo')+"/"
	if os.path.exists(DOSSIER_UPS):
		return (DOSSIER_UPS)
	else:
		os.mkdir(DOSSIER_UPS)
		return (DOSSIER_UPS)