# -*- coding:Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

import time

import RPG_saveload as memory
import RPG_histoire as story
import RPG_graph as gui

####----####----####----####----####
##############Function##############
####----####----####----####----####

def game(joueur, inv_joueur, man_loot, man_mob):
    jouer = True
    print ("Bienvenue dans un micro RPG\n\n")

    menu = gui.Gui_main()
    while menu.play :
        menu.menu(joueur, inv_joueur, man_mob, man_loot)
        #print("Que souhaitez vous faire ?\n")
        #print("1. Partir en quête")
        #print("2. Partir dans un village")
        #print("3. Dormir")
        #print("4. Regarder votre équipement")
        #print("5. Vider son inventaire par-terre..")
        #print("6. Arrêter le jeu")
        # choix = input()
        # if choix == "1":
        #     print ("Vous êtes parti en quête")
        #     i = story.quete(joueur, man_mob)
        #     if i == 0:
        #         print ("Vous avez rien loot")
        #     else:
        #         drop = man_loot.loot()
        #         gui.Gui_loot(drop)
        #         inv_joueur.ajout_item(drop)
        # elif choix == "2":
        #     print("Vous êtes dans le village")
        #     print("C'est ici que vous pouvez changer d'équipement")
        #     print("Vous êtes équipé de :")
        #     joueur.voir_stuff()
        #     print("Vous avez dans votre inventaire :")
        #     inv_joueur.afficher()
        #     print("\n\n")
        #     joueur.swap_stuff(inv_joueur)
        # elif choix == "3":
        #     print ("Vous vous endormez")
        #     print("Vous regagnez tout vos point de vie")
        #     joueur.pv = 200
        # elif choix == "4":
        #     print("Vous êtes équipé de :")
        #     joueur.voir_stuff()
        # elif choix == "5":
        #     print("Êtes-vous sur ? yes // no")
        #     choix = input()
        #     if choix == "yes":
        #         inv_joueur.clean()
        #         print("Bah .. on peut dire que tu es plus léger..")
        #     else:
        #         print("Bonne idée! les objets sont dur à avoir ..")
        # elif choix == "6":
        #     print("Le jeu s'arrête dans 1 secondes")
        #     time.sleep (1)
        #     memory.save(joueur, inv_joueur)
        #     inv_joueur.afficher()
        #     jouer = False
        # else:
        #     print("Mauvaise valeur entrée")

def game_loop():
    pass