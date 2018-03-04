# -*- coding:Utf-8 -*-
from os import path
from os import getcwd
from os import mkdir
import sys
import configparser
import pickle



def create_save_directory(): 
    curdir = path.dirname(__file__)
    if len(curdir) == 0: 
        curdir = getcwd()
    if not path.exists(path.join(curdir,'Save')):
        mkdir(path.join(curdir,'Save'))

def create_ini(chemin, nom, password):
	ini_player = configparser.ConfigParser()
	if not path.isfile(chemin):
		print("Pas de compte trouvé sur cet ordinateur")		
		ini_player.read(chemin)
		ini_player.add_section(nom)
		ini_player.set(nom, "password", password)
		ini_player.set(nom, "Date_creation", "01/01/2017")
		ini_player.set(nom, "Nb_lancement", "1")
		ini_player.set(nom, "Last_connextion", "01/01/2017")
		ini_player.write(open(chemin,"w"))
	else:
		print("Le jeu à déjà était utilisé")
		ini_player.read(chemin)
		liste_joueur = ini_player.sections()
		for item in liste_joueur:
			if str(item) == nom:
				print("Nom de joueur déjà existant")
				sys.exit(0)
		ini_player.add_section(nom)
		ini_player.set(nom, "password", password)
		ini_player.set(nom, "Date_creation", "01/01/2017")
		ini_player.set(nom, "Nb_lancement", "1")
		ini_player.set(nom, "Last_connextion", "01/01/2017")
	ini_player.write(open(chemin,"w"))

def load_ini(chemin, nom, password):
	ini_player = configparser.ConfigParser()
	ini_player.read(chemin)
	liste_joueur = ini_player.sections()
		
	for item in liste_joueur:
		if str(item) == str(nom):
			test_password = ini_player.get(nom, "password")
			if password == test_password:
				print("Login correct")			
				with open(nom + ".rpg",'rb') as fichier:
					load_joueur = pickle.Unpickler(fichier)
					joueur = load_joueur.load()
					inventaire = load_joueur.load()
					break
			else:
				print("Wrong Password")
				sys.exit(0)

	return joueur, inventaire

def save(chemin, joueur, inventaire):
	ini_player = configparser.ConfigParser()
	ini_player.read(chemin)
	nom = joueur.nom
	print(nom)


	ini_player.set(nom, "Date_creation", "01/01/2017")
	ini_player.set(nom, "Nb_lancement", "2")
	ini_player.set(nom, "Last_connextion", "01/01/2017")
	ini_player.write(open(chemin,"w"))

	with open(joueur.nom + ".rpg",'wb') as fichier:
		save_joueur = pickle.Pickler(fichier)
		save_joueur.dump(joueur)
		save_joueur.dump(inventaire)
		print("Sauvegarde effectué")
