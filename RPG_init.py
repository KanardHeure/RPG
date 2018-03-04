# -*- coding:Utf-8 -*-
from os import path
import json

import RPG_SDL as manager
from RPG_function import *



def create_manager():
    curdir = path.dirname(__file__)
    chemin = []
    chemin.append(path.abspath(path.join(curdir,'armes.json')))
    chemin.append(path.abspath(path.join(curdir,'armures.json')))
    chemin.append(path.abspath(path.join(curdir,'mob.json')))
    chemin.append(path.abspath(path.join(curdir,'save.ini')))

    manager_armes = manager.ManagerArmes()
    manager_armures = manager.ManagerArmures()
    manager_mob = manager.ManagerMob()

    for json_armes in json.load(open(chemin[0])):
        armes = Arme(**json_armes)
        manager_armes.load(armes)

    for json_armures in json.load(open(chemin[1])):
        armures = Armure(**json_armures)
        manager_armures.load(armures)

    for json_mob in json.load(open(chemin[2])):
        mob = Monstre(**json_mob)
        manager_mob.load(mob)

    return manager_armes, manager_armures, manager_mob, chemin

