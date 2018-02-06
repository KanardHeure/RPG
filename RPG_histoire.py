# -*- coding:Utf-8 -*-
from RPG_function import *
from RPG_SDL import *
from RPG_graph import *
from RPG_combat import *

def quete(j, m):
	index = 0
	game_error = False


	print("Vous vous réveillez dans un lieu très sombre avec l'esprit très embrumé ..")
	print("1. Vous observez autour de vous ?")
	print("2. Vous vérifiez que vous êtes en entier ?")
	print("3. Vous essayez de vous souvenir comment vous en êtes arrivé la ?")
	choix = input()
	if choix == "1":
		random_effect(2)
		while not game_error:
			game_error = not game_error
			if index == 0:
				print("En observant autour de vous, vous voyez un ennemie")
				print(m.name + " " + str(m.pv))
				Combat(j,m)
				return 0
			elif index == 1:
				print("En observant autour de vous, vous voyez un petit coffre")
				return 1
			elif index == 2:
				print("En observant autour de vous, vous observez .. rien de spécial")
				return 0
			else:
				print("Error")
				game_error = not game_error
	if choix == "2":
		random_effect(1)
		while not game_error:
			game_error = not game_error
			if index == 0:
				print("Deux bras .. Deux jambes .. C'est bon tout va bien ..")
				return 0
			elif index == 1:
				print("Qu'est-ce que toute ces blessures ..")
				print("Vous perdez 5 point de vie")
				return 0
			else:
				print("Error")
				game_error = not game_error

def random_effect(nb):
	index = random.randint(0, 0)


		