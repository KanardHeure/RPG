# -*- coding:Utf-8 -*-
from RPG_function import *
from RPG_SDL import *
from RPG_graph import *
from RPG_histoire import *
from os import path
from os import getcwd
from os import mkdir
from tkinter import *
import time

# Chargement des armes, armures, monstres à partir des json

curdir = path.dirname(__file__)
if len(curdir) == 0: curdir = getcwd()

if not path.exists(path.join(curdir,'Save')):
	mkdir(path.join(curdir,'Save'))

chemin = []
chemin.append(path.abspath(path.join(curdir,'armes.json')))
chemin.append(path.abspath(path.join(curdir,'armures.json')))



manager_armes = ManagerArmes()
manager_armures = ManagerArmures()






for json_armes in json.load(open(chemin[0])):
	armes = Arme(**json_armes)
	manager_armes.load(armes)

for json_armes in json.load(open(chemin[1])):
	armes = Armure(**json_armes)
	manager_armures.load(armes)



chemin_mob = path.abspath(path.join(curdir,'mob.json'))
manager_mob = ManagerMob(chemin_mob)

# Initialisation des caractérisques du joueur

chemin = path.abspath(path.join(curdir,'save.ini'))
player = Gui_initialize_player(chemin)


if player.loadplayer == True:
	joueur = player.joueur
	inv_joueur = player.inventaire
else:
	joueur = RPG_function.Joueur(player, manager_armes, manager_armures)
	inv_joueur = Inventaire()

jouer = True

print ("Bienvenue dans un micro RPG\n\n")
loot = ManagerLoot(manager_armes, manager_armures)

while jouer:
	print ("Que souhaitez vous faire ?\n")
	print ("1. Partir en quête")
	print ("2. Partir dans un village")
	print ("3. Dormir")
	print ("4. Regarder votre équipement")
	print ("5. Arrêter le jeu")
	choix = input()
	if choix == "1":
		print ("Vous êtes parti en quête")
		monstre = manager_mob.get_random_mob()
		print(type(monstre))
		monstre.create(joueur.lvl)
		i = quete(joueur,monstre)
		if i == 0:
			print (" Vous avez rien loot")
		else:
			drop = loot.loot()
			Gui_loot(drop)
			inv_joueur.ajout_item(drop)
	elif choix == "2":
		print ("Vous êtes dans le village")
	elif choix == "3":
		print ("Vous vous endormez")
	elif choix == "4":
		joueur.voir_stuff()
	elif choix == "5":
		print("Le jeu s'arrête dans 1 secondes")
		time.sleep (1)
		player.save(joueur, inv_joueur)
		inv_joueur.afficher()
		jouer = False
	else:
		print("Mauvaise valeur entrée")

