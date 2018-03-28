# -*- coding:Utf-8 -*-
from tkinter import *
from os import path
from os import chdir
from os import getcwd
import configparser
import time

import RPG_saveload as memory
import RPG_histoire as story
from RPG_function import *
import RPG_saveload


class Gui_initialize_player():
    def __init__(self, chemin, manager_armes, manager_armures):
        self.man_armes = manager_armes
        self.man_armures = manager_armures
        self.joueur = None
        self.inventaire = None
        self.chemin = chemin
        self.cfg_joueur = configparser.ConfigParser()
        self.fenetre = Tk()
        self.fenetre.geometry("250x100+250+250")
        self.loadplayer = False

        curdir = getcwd()
        chem1 = path.abspath(path.join(curdir,'Save/'))
        chdir(chem1)

        self.label = Label(self.fenetre,text ="Bienvenue dans le Kanard RPG")
        self.inscription = Button(self.fenetre,text ="Sign In", command = self._on_sign_in)
        self.chargement = Button(self.fenetre,text="Log In", command = self._on_log_in)
        self.label.place(x = 25,y = 10, height = 20, width = 200)
        self.inscription.place(x = 20, y = 50, height = 30, width = 90)
        self.chargement.place(x = 140, y = 50, height = 30, width = 90)
        self.fenetre.mainloop()

    def _GUI_log(self):
        ### --- Destruction des items de la fenêtre précédente --- ###
        self.inscription.destroy()
        self.chargement.destroy()
        ### ------------------------------------------------------ ###
        self.nom = StringVar()
        self.password = StringVar()
        self.labelps = Label(self.fenetre,text ="Pseudo : ")
        self.zone_nom = Entry(self.fenetre, textvariable = self.nom)
        self.labelpa = Label(self.fenetre, text ="Mdp : ")
        self.zone_psd = Entry(self.fenetre, textvariable = self.password)
        self.labelps.place(x = 20, y = 40, height = 20, width = 50)
        self.labelpa.place(x = 20, y = 70, height = 20, width = 50)  
        self.zone_nom.place(x = 120, y = 40, height = 20, width = 110)
        self.zone_psd.place(x = 120, y = 70, height = 20, width = 110)     

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
        self.joueur, self.inventaire = RPG_saveload.load(self.nom, password)

    def _init_perso(self, event):
        self.nom = self.nom.get()
        password = self.password.get()

        if (self.nom == "") or (password == ""):
            print("Tu as oublié un champ gros boulet")
            time.sleep(3)
            sys.exit(0)

        RPG_saveload.create_ini(self.nom, password)
        self.joueur = Joueur(self.nom, self.man_armes, self.man_armures)
        self.inventaire = Inventaire()
        self.fenetre.destroy()

class Gui_loot():
    def __init__(self, drop):
        self.fenetre = Tk()
        self.fenetre.geometry("300x90+250+250")
        label = Label(self.fenetre,text ="Félicitation vous avez loot : {}".format(drop.nom))
        bouton_loot = Button(self.fenetre, text ="Super !!", command = self.fenetre.destroy)
        label.place(x = 20, y = 10, height = 25, width = 260)   
        bouton_loot.place(x = 110, y = 50, height = 25, width = 80)
        self.fenetre.mainloop()

class Gui_switch_arme():
    pass

class Gui_main():
    pass
    def __init__(self):
        self.play = True


    def menu(self, joueur, inv_joueur, man_mob, man_loot):
        self.fenetre = Tk()
        self.fenetre.geometry("400x300+50+50")
        self.joueur = joueur
        self.inv_joueur = inv_joueur
        self.man_mob = man_mob
        self.man_loot = man_loot

        self.label_localisation = Label(self.fenetre, text ="Vous êtes actuellement __")
        self.label_choix = Label(self.fenetre, text ="Que souhaitez-vous faire ?")
        self.label_quete = Label(self.fenetre, text ="Partir en quête")
        self.label_village = Label(self.fenetre, text ="Allez au village")
        self.label_dormir = Label(self.fenetre, text ="Dormir")
        self.label_regarder = Label(self.fenetre, text ="Regarder votre équipement")
        self.label_sac = Label(self.fenetre, text ="Vider votre sac")
        self.label_quitter = Label(self.fenetre, text ="Sauvegarder et Quitter")

        self.button_quete = Button(self.fenetre, text ="Allez", command = self.quete)
        self.button_village = Button(self.fenetre, text ="Allez", command = self.village)
        self.button_dormir = Button(self.fenetre, text ="Allez", command = self.dormir)
        self.button_regarder =Button(self.fenetre, text ="Allez", command = self.regarder)
        self.button_sac = Button(self.fenetre, text ="Allez", command = self.sac)
        self.button_quitter = Button(self.fenetre, text ="Allez", command = self.quitter)

        self.label_localisation.place(x = 50,y = 10, height = 20, width = 300)
        self.label_choix.place(x = 50,y = 40, height = 20, width = 300)
        self.label_quete.place(x = 30,y = 70, height = 20, width = 200)
        self.label_village.place(x = 30,y = 100, height = 20, width = 200)
        self.label_dormir.place(x = 30,y = 130, height = 20, width = 200)
        self.label_regarder.place(x = 30,y = 160, height = 20, width = 200)
        self.label_sac.place(x = 30,y = 190, height = 20, width = 200)
        self.label_quitter.place(x = 30,y = 220, height = 20, width = 200)

        self.button_quete.place(x = 250,y = 70, height = 20, width = 50)
        self.button_village.place(x = 250,y = 100, height = 20, width = 50)
        self.button_dormir.place(x = 250,y = 130, height = 20, width = 50)
        self.button_regarder.place(x = 250,y = 160, height = 20, width = 50)
        self.button_sac.place(x = 250,y = 190, height = 20, width = 50)
        self.button_quitter.place(x = 250,y = 220, height = 20, width = 50)

        self.fenetre.mainloop()

    def quete(self):
        self.fenetre.destroy()
        i = story.quete(self.joueur, self.man_mob)
        if i == 0:
            print ("Vous avez rien loot")
        else:
            drop = self.man_loot.loot()
            Gui_loot(drop)
            self.inv_joueur.ajout_item(drop)

    def village(self):
        pass
        self.fenetre.destroy()

    def dormir(self):
        pass
        self.fenetre.destroy()

    def regarder(self):
        pass
        self.fenetre.destroy()

    def sac(self):
        pass
        self.fenetre.destroy()

    def quitter(self):
        self.fenetre.destroy()
        self.play = False
        memory.save(self.joueur, self.inv_joueur)
        self.inv_joueur.afficher()

    def _destroy_menu(self):
        self.label_localisation.destroy()
        self.label_choix.destroy()
        self.label_quete.destroy()
        self.label_village.destroy()
        self.label_dormir.destroy()
        self.label_regarder.destroy()
        self.label_sac.destroy()
        self.label_quitter.destroy()
        self.button_quete.destroy()
        self.button_village.destroy()
        self.button_dormir.destroy()
        self.button_regarder.destroy()
        self.button_sac.destroy()
        self.button_quitter.destroy()

