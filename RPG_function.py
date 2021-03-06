# -*- coding:Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

import random

####----####----####----####----####
##############Function##############
####----####----####----####----####

class Joueur():
    "Création d'un joueur"
    def __init__(self, nom, man_arme, man_armure, pv = 200, mana = 50):

        #__INFO__
        self.nom = nom
        self.lvl = 1
        self.exp = 0
        self.pv = 200
        self.mana = 50
        self.argent = 0
        #__STUFF__ 
        self.arme = man_arme.get_arme(1)
        self.tete = man_armure.get_armure(["tete", 1])
        self.torse = man_armure.get_armure(["torse", 1])
        self.jambiere = man_armure.get_armure(["jambe", 1])
        self.botte = man_armure.get_armure(["pied",1])
        self.gant = man_armure.get_armure(["main", 1])
        self.epaule = man_armure.get_armure(["epaule", 1])
        self.armure = self.tete.protection + self.torse.protection + self.jambiere.protection + self.botte.protection + self.gant.protection + self.epaule.protection
        #__CARACTERISTIQUE__
        self.speed = 10
        self.force = self.arme.degat

    def swap_stuff(self, inventaire):
        print("Voulez-vous changer d'arme?\n")
        answer = input("yes or no ")
        if answer == "yes":
            list_arme = []
            for item in inventaire.inventaire:
                if item.type == "weapon":
                    list_arme.append(item)
            if len(list_arme) == 0:
                print("Vous n'avez pas d'armes dans votre inventaire")
            else:
                for indice, arme in enumerate(list_arme):
                    print(indice, arme.nom)

                print("Quel arme souhaitez-vous équiper?")
                index = int(input())
                self.changement_arme(list_arme[index])
        else:
            print("Pas de changement d'arme")

    def changement_arme(self, new_arme):
        self.arme = new_arme
        self.force = self.arme.degat

    def changement_armure(self, new_armure):
        if new_armure.Lieu == "tete":
            self.tete = new_armure
        elif new_armure.Lieu == "torse":
            self.torse = new_armure
        elif new_armure.Lieu == "jambe":
            self.jambiere = new_armure
        elif new_armure.Lieu == "main":
            self.gant = new_armure
        elif new_armure.Lieu == "epaule":
            self.epaule = new_armure
        elif new_armure.Lieu == "botte":
            self.botte = new_armure
        else:
            print("ERROR, Ce n'est pas armure")

    def voir_stuff(self):
        print("Vous portez: ")
        print(self.tete.nom)
        print(self.torse.nom)
        print(self.jambiere.nom)
        print(self.botte.nom)
        print(self.gant.nom)
        print(self.epaule.nom)
        print("Votre arme: ")
        print(self.arme.nom)

class Monstre():
    "Création d'un monstre"
    def __init__(self, **attribut):
        for attr_name, attr_value in attribut.items():
            setattr(self, attr_name, attr_value)

    def create(self, lvl_j):
        i = random.randint(1,100)
        if i <= 5:
            self.name = "** BOSS ** " + self.nom
            self.pv = self.pv*(1.5)**(4 + lvl_j)
            self.force = self.force + self.force*(0.3)**(5+lvl_j)
            self.resistance = self.resistance + self.resistance*0.25*lvl_j
            self.xp = self.xp*2*(lvl_j + (lvl_j/10))
        if i > 5 and i <= 15:
            self.name = self.nom + " Elite" 
            self.pv = self.pv*(1.5)**(2 + lvl_j)
            self.force = self.force + self.force*(0.3)**(3+lvl_j)
            self.resistance = self.resistance + self.resistance*0.10*lvl_j
            self.xp = self.xp*1.5*(lvl_j + (lvl_j/10))
        if i > 15 and i <= 90:
            self.name = self.nom            
            self.pv = self.pv*(1.5)**(lvl_j)
            self.force = self.force + self.force*(0.3)**(lvl_j)
            self.resistance = self.resistance
            self.xp = self.xp*(lvl_j + (lvl_j/10))
        if i > 90:
            self.name = self.nom + " Faible" 
            self.pv = self.pv*(1.5)**(lvl_j - 1)
            self.force = self.force + self.force*(0.3)**(lvl_j-1)
            self.resistance = self.resistance - self.resistance*0.10
            self.xp = self.xp*0.9*(lvl_j + (lvl_j/10))      

class Stuff():
    "Création d'une pièce d'équipement"
    def __init__(self, nom, valeur, n_id):
        self.nom = nom
        self.valeur = valeur
        self.id = n_id

class Arme():
    "Création d'une arme"
    def __init__(self, **attribut):
        for attr_name, attr_value in attribut.items():
            setattr(self, attr_name, attr_value)

class Armure():
    "Création d'une armure"
    def __init__(self, **attribut):
        for attr_name, attr_value in attribut.items():
            setattr(self, attr_name, attr_value)

class Inventaire():
    "Création d'un inventaire"
    def __init__(self):
        self.inventaire = []
    def ajout_item(self, loot):
        self.inventaire.append(loot)
    def suppr_item(self, ID):
        del self.inventaire [ID]
    def afficher(self):
        i = 0
        for item in self.inventaire:
            print("{} :  {}".format(i,item.nom))
            i= i +1
    def clean(self):
        self.inventaire.clear()



class Sort():
    "Création d'un sort"
    def __init__(self,cout,nom):
        self.mana = cout
        self.nom = nom

class SortSoin(Sort):
    "Création d'un sort de soin"
    def __init__(self,cout, nom,heal):
        Sort.__init__(self,cout,nom)
        self.soin = heal

class SortDgt(Sort):
    "Création d'un sort de dégâts"
    def __init__(self,cout,nom):
        Sort.__init__(self,nom)
        self.degat = degat



def lancerSoin(sort,lanceur):
    lanceur.pv = lanceur.pv + sort.soin
    print("{0} utilise {1} et récupère {2} points de vie.".format(lanceur.nom,sort.nom,sort.soin))
    print ("{0} a {1} point de vie.".format(lanceur.nom,lanceur.pv))

def lancerSortilege(sort,lanceur,defenseur):
    lanceur.mana = lanceur.mana - sort.mana
    defenseur.pv = defenseur.pv - sort.degat
    print("")
    print("")