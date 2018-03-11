# -*- coding:Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

import RPG_saveload as memory
import RPG_graph as gui
import RPG_game as game

####----####----####----####----####
##############Function##############
####----####----####----####----####

def main():
    memory.create_save_directory()
    manager_armes, manager_armures, manager_mobs, chemin = memory.init_manager()
    player = gui.Gui_initialize_player(chemin[3], manager_armes, manager_armures)
    joueur = player.joueur
    inv_joueur = player.inventaire
    manager_loot = memory.ManagerLoot(manager_armes, manager_armures)
    game.game(joueur, inv_joueur, manager_loot, manager_mobs)


if __name__ == "__main__":
    main()
else:
    print("Le script main.py est uniquement fait pour être lancé")