# -*- coding:Utf-8 -*-
from tkinter import *
from os import path
from os import chdir
from os import getcwd
import configparser
from RPG_function import *
import sys
import time
import RPG_function
import pickle


class Gui_initialize_player():
	def __init__(self, chemin):

		self.chemin = chemin
		self.cfg_joueur = configparser.ConfigParser()
		self.fenetre = Tk()
		self.fenetre.geometry("250x100+50+50")
		self.loadplayer = False

		curdir = getcwd()
		chem1 = path.abspath(path.join(curdir,'Save/'))
		chdir(chem1)

		label = Label(self.fenetre,text ="Bienvenue dans le Kanard RPG")
		inscription = Button(self.fenetre,text ="Sign In", command = self._on_sign_in)
		chargement = Button(self.fenetre,text="Log In", command = self._on_log_in)
		label.place(x = 25,y = 10, height = 20, width = 200)
		inscription.place(x = 20,y = 50, height = 30, width = 90)
		chargement.place(x = 140,y = 50, height = 30, width = 90)
		self.fenetre.mainloop()

	def _GUI_log(self):
		self.fenetre.destroy()
		self.fenetre = Tk()
		self.nom = StringVar()
		self.password = StringVar()
		self.labelps = Label(self.fenetre,text ="Pseudo : ")
		self.zone_nom = Entry(self.fenetre, textvariable = self.nom)
		self.labelpa = Label(self.fenetre, text ="Mdp : ")
		self.zone_psd = Entry(self.fenetre, textvariable = self.password)
		self.labelps.grid(row = 0 ,column = 0)
		self.labelpa.grid(row = 1, column = 0)	
		self.zone_nom.grid(row = 0, column = 1)
		self.zone_psd.grid(row = 1, column = 1)		

	def _on_sign_in(self):
		self._GUI_log()
		self.zone_psd.bind("<Return>", self._init_perso)
		self.zone_nom.bind("<Return>", self._init_perso)		
		self.fenetre.mainloop()

	def _on_log_in(self):
		self._GUI_log()
		self.zone_psd.bind("<Return>", self._load_perso)
		self.zone_nom.bind("<Return>", self._load_perso)		
		self.fenetre.mainloop() 
		
	def _load_perso(self, event):
		self.fenetre.destroy()
		self.nom = self.nom.get()
		wrong_name = False
		self.cfg_joueur.read(self.chemin)
		self.liste_joueur = self.cfg_joueur.sections()
		self.loadplayer = True
		
		for item in self.liste_joueur:
			if str(item) == self.nom:
				test_password = self.cfg_joueur.get(self.nom, "password")
				password = self.password.get()
				if password == test_password:
					print("Login correct")			
					with open(self.nom + ".rpg",'rb') as fichier:
						load_joueur = pickle.Unpickler(fichier)
						self.joueur = load_joueur.load()
						self.inventaire = load_joueur.load()
						wrong_name = False
						break
				else:
					print("Mdp incorrect")
					time.sleep(3)
					sys.exit(0)
			else:
				wrong_name = True
				print ("test")
		if wrong_name :
			print("Nom incorrect")
			time.sleep(3)
			sys.exit(0)

	def _init_perso(self, event):
		self.nom = self.nom.get()
		password = self.password.get()

		if (self.nom == "") or (password == ""):
			print("Tu as oublié un champ gros boulet")
			time.sleep(3)
			sys.exit(0)

		if not path.isfile(self.chemin):
			print("Pas de compte trouvé sur cet ordinateur")		
			self.cfg_joueur.read(self.chemin)
			self.cfg_joueur.add_section(self.nom)
			self.cfg_joueur.set(self.nom, "password", password)
			self.cfg_joueur.set(self.nom, "Date_creation", "01/01/2017")
			self.cfg_joueur.set(self.nom, "Nb_lancement", "1")
			self.cfg_joueur.set(self.nom, "Last_connextion", "01/01/2017")
			self.cfg_joueur.write(open(self.chemin,"w"))
		else:
			print("Le jeu à déjà était utilisé")
			self.cfg_joueur.read(self.chemin)
			self.liste_joueur = self.cfg_joueur.sections()
			for item in self.liste_joueur:
				if str(item) == self.nom:
					print("Nom de joueur déjà existant")
					time.sleep(3)
					sys.exit(0)
			self.cfg_joueur.add_section(self.nom)
			self.cfg_joueur.set(self.nom, "password", password)
			self.cfg_joueur.set(self.nom, "Date_creation", "01/01/2017")
			self.cfg_joueur.set(self.nom, "Nb_lancement", "1")
			self.cfg_joueur.set(self.nom, "Last_connextion", "01/01/2017")


		self.cfg_joueur.write(open(self.chemin,"w"))
		self.fenetre.destroy()	
				
	def save(self, joueur, inventaire):

		self.cfg_joueur.set(self.nom, "Date_creation", "01/01/2017")
		self.cfg_joueur.set(self.nom, "Nb_lancement", "2")
		self.cfg_joueur.set(self.nom, "Last_connextion", "01/01/2017")
		self.cfg_joueur.write(open(self.chemin,"w"))


		with open(self.nom + ".rpg",'wb') as fichier:
			save_joueur = pickle.Pickler(fichier)
			save_joueur.dump(joueur)
			save_joueur.dump(inventaire)
			print("Sauvegarde effectué")


class Gui_loot():
	def __init__(self, drop):
		self.fenetre = Tk()
		label = Label(self.fenetre,text ="Félicitation vous avez loot : {}".format(drop.nom))
		bouton_loot = Button(self.fenetre,text ="Super !!", command = self.fenetre.destroy)
		label.grid(row=0)	
		bouton_loot.grid(row =1)
		self.fenetre.mainloop()


class Gui_switch_arme():
	pass
