# -*- coding:utf-8 -*-
"""uploadIMageDAO"""
import os
from flask import session




def createDirectory():
	"""This function creatrs a directory"""
	dossier = '/Applications/PythonPublisher/static/'+session.get('pseudo')+"/"
	if os.path.exists(dossier):
		return dossier
	else:
		os.mkdir(dossier)
	return dossier
