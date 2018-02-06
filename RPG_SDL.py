# -*- coding: utf-8 -*-
from os import path
import json
import random
import RPG_function


class ManagerArmes():
	def __init__(self, chemin):
		self.armes = []
		self.chemin = chemin
		self.load()

	def load(self):
		self.armes.clear()
		if not path.isfile(self.chemin):
			print("Impossible de trouver le fichier: armes.json")
		with open(self.chemin, "r") as fichier:
			armes_json = json.load(fichier)
			for item in armes_json:
				arme = RPG_function.Arme(item["nom"], item["valeur"] , item["ID"], item["degat"])
				self.armes.append(arme)

	def get_random_arme(self):
		self.load()
		arme_index = random.randint(0, len(self.armes) - 1)
		return self.armes[arme_index]

	def get_arme(self, n_id):
		for item in self.armes:
			if n_id == item.id:
				print ("arme trouvé")
				return item
		print("arme introuvable")


class ManagerMob():
	def __init__(self, chemin):
		self.mob = []
		self.chemin = chemin
		self.load()
	def load(self):
		self.mob.clear()
		if not path.isfile(self.chemin):
			print("Impossible de trouver le fichier: mob.json")
		with open (self.chemin, "r") as fichier:
			mob_json = json.load(fichier)
			for item in mob_json:
				mob = RPG_function.Monstre(item["nom"], item["pv"], item["mana"], item["speed"], item["force"], item["resistance"], item["xp"], item["race"])
				self.mob.append(mob)

	def get_random_mob(self):
		self.load()
		mob_index = random.randint(0, len(self.mob) - 1)
		print("Nouveau monstre")
		return self.mob[mob_index]


class ManagerArmures():
	def __init__(self, chemin):
		self.armure = []
		self.chemin = chemin
		self.load()

	def load(self):
		self.armure.clear()
		if not path.isfile(self.chemin):
			print("Impossible de trouver le fichier: armures.json")
		with open (self.chemin, "r") as fichier:
			armure_json = json.load(fichier)
			for item in armure_json:
				armure = RPG_function.Armure(item["nom"], item["valeur"], item["ID"], item["protection"], item["Lieu"])
				self.armure.append(armure)

	def get_random_armure(self):
		self.load()
		armure_index = random.randint(0, len(self.armure) - 1)
		return self.armure[armure_index]

	def get_armure(self, lieu_id):
		for item in self.armure:
			if item.lieu == lieu_id[0]:
				if item.id == int(lieu_id[1]):
					print(item.nom)
					return item


class ManagerLoot():
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

			

