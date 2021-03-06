# -*- coding:Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####



def Combat(joueur, monstre):

    speed_joueur = joueur.speed
    speed_monstre = monstre.speed

    while True:

        while speed_joueur < 100 or speed_monstre < 100:
            speed_joueur = speed_joueur + joueur.speed
            speed_monstre = speed_monstre + monstre.speed

        if speed_joueur >= 100:
            speed_joueur = speed_joueur - 100
            Attaque(joueur, monstre)
            if Mort(joueur, monstre):
                break

        if speed_monstre >= 100:
            speed_monstre = speed_monstre - 100
            Attaque(monstre, joueur)
            if Mort(joueur, monstre):
                break


def Attaque(attaquant, defenseur):
    defenseur.pv = int(defenseur.pv) - int(attaquant.force) 
    print ("{0} attaque {1} et lui inflige {2} dégats.".format(attaquant.nom, defenseur.nom, int(attaquant.force)))
    if defenseur.pv > 0:
        print ("Il reste {0} hp à {1}.".format(defenseur.pv, defenseur.nom))
    else:
        print("Il reste 0 hp à {0}.".format(defenseur.nom))

def Mort(joueur, monstre):
    if joueur.pv < 1:
        print("Vous êtes mort")
        return True
    if monstre.pv < 1:
        print("Vous avez tué le monstre")
        return True
    return False
