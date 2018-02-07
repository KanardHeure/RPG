# -*- coding: utf-8 -*-
from os import path
import json
import random
import RPG_function
import copy

class ManagerArmes():
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

class ManagerMob():
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

			

