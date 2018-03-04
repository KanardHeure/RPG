# -*- coding:Utf-8 -*-
from tkinter import *
from os import path
from os import chdir
from os import getcwd
import configparser
from RPG_function import *
import time
import RPG_function

import RPG_saveload


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
		password = self.password.get()
		self.joueur, self.inventaire = RPG_saveload.load_ini(self.chemin, self.nom, password)
		self.loadplayer = True

	def _init_perso(self, event):
		self.nom = self.nom.get()
		password = self.password.get()

		if (self.nom == "") or (password == ""):
			print("Tu as oublié un champ gros boulet")
			time.sleep(3)
			sys.exit(0)

		RPG_saveload.create_ini(self.chemin, self.nom, password)
		self.fenetre.destroy()


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
