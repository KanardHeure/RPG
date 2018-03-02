# -*- coding:Utf-8 -*-
from RPG_function import *
from RPG_SDL import *
from RPG_graph import *
from RPG_histoire import *
import RPG_init as init

from tkinter import *
import time

# Chargement des armes, armures, monstres à partir des json
init.create_save_directory()
manager_armes, manager_armures, manager_mob, chemin = init.create_manager()
# Initialisation des caractérisques du joueur

player = Gui_initialize_player(chemin[3])

if player.loadplayer == True:
    joueur = player.joueur
    inv_joueur = player.inventaire
else:
    joueur = RPG_function.Joueur(player, manager_armes, manager_armures)
    inv_joueur = Inventaire()


# Lancement du jeu

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
		print("Vous êtes dans le village")
		print("C'est ici que vous pouvez changer d'équipemnt")
		print("Vous êtes équipé de :")
		joueur.voir_stuff()
		print("Vous avez dans votre inventaire :")
		inv_joueur.afficher()
		print("\n\n")
		joueur.swap_stuff(inv_joueur)
	elif choix == "3":
		print ("Vous vous endormez")
		print("Vous regagnez tout vos point de vie")
		joueur.pv = 200
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


