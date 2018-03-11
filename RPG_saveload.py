# -*- coding:Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

from os import path
from os import getcwd
from os import mkdir
import random
import configparser
import sys
import pickle
import copy
import json

import RPG_function as func

####----####----####----####----####
##############Function##############
####----####----####----####----####

class ManagerArmes():
    "Création d'un obj/liste qui contient toutes les armes"
    def __init__(self):
        self.armes = []

    def load(self, arme):
        self.armes.append(arme)

    def get_random_arme(self):
        arme_index = random.randint(0, len(self.armes) - 1)
        return self.armes[arme_index]

    def get_arme(self, n_id):
        for item in self.armes:
            if n_id == item.ID:
                print ("arme trouvé")
                return item
        print("arme introuvable")

    def _afficher_tout(self):
        for arme in self.armes:
            print(arme.nom)

class ManagerMobs():
    "Création d'un obj/list qui contient tout les monstres"
    def __init__(self):
        self.mob = []

    def load(self, monstre):
        self.mob.append(monstre)

    def get_random_mob(self):
        mob_index = random.randint(0, len(self.mob) - 1)
        print("Nouveau monstre")
        copy_mob = copy.deepcopy(self.mob[mob_index])
        return copy_mob

class ManagerArmures():
    "Création d'un obj/list qui contient toutes les armures"
    def __init__(self):
        self.armure = []

    def load(self, armure):
        self.armure.append(armure)

    def get_random_armure(self):
        armure_index = random.randint(0, len(self.armure) - 1)
        return self.armure[armure_index]

    def get_armure(self, lieu_id):
        for item in self.armure:
            if item.Lieu == lieu_id[0]:
                if item.ID == int(lieu_id[1]):
                    print(item.nom)
                    return item

class ManagerLoot():
    "Gestionnaire aléatoire de loot"
    def __init__(self, arme, armure):
        
        self.arme = arme
        self.armure = armure

    def loot(self):
        self.index_loot = random.randint(0,1)
        if self.index_loot == 0:
            arme_loot = self.arme.get_random_arme()
            return arme_loot
        elif self.index_loot == 1:
            armure_loot = self.armure.get_random_armure()
            return armure_loot
        else:
            print("ERROR")

def create_save_directory():
    "Créer un répertoire 'save' à la racine du script"
    curdir = path.dirname(__file__)
    if len(curdir) == 0: 
        curdir = getcwd()
    if not path.exists(path.join(curdir,'Save')):
        mkdir(path.join(curdir,'Save'))

def create_ini(nom, password):
    "Création d'un fichier .ini par joueur"
    chemin = init_chemin()
    chemin = chemin[3]
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

def load(nom, password):
    "Chargement d'une sauvegarde"
    chemin = init_chemin()
    chemin = chemin[3]
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

def save(joueur, inventaire):
    "Sauvegarde du personnage via pickle"
    chemin = init_chemin()
    chemin = chemin[3]
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

def init_chemin():
    "Création d'une liste ou se trouve tout les chemins importants"
    curdir = path.dirname(__file__)
    chemin = []
    chemin.append(path.abspath(path.join(curdir,'armes.json')))
    chemin.append(path.abspath(path.join(curdir,'armures.json')))
    chemin.append(path.abspath(path.join(curdir,'mob.json')))
    chemin.append(path.abspath(path.join(curdir,'save.ini')))
    return chemin

def init_manager():
    "Initialise tout les objets/listes via les json"
    chemin = init_chemin()
    manager_armes = ManagerArmes()
    manager_armures = ManagerArmures()
    manager_mobs = ManagerMobs()

    for json_armes in json.load(open(chemin[0])):
        armes = func.Arme(**json_armes)
        manager_armes.load(armes)

    for json_armures in json.load(open(chemin[1])):
        armures = func.Armure(**json_armures)
        manager_armures.load(armures)

    for json_mob in json.load(open(chemin[2])):
        mob = func.Monstre(**json_mob)
        manager_mobs.load(mob)

    return manager_armes, manager_armures, manager_mobs, chemin