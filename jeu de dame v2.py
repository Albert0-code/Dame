#################################################################################
#                                                                                                               Jeu de dame                                                                                                                                                        #
#################################################################################

plateau = [[1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [2,0,2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2,0,2],
           [2,0,2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2,0,2]]

## Test pour savoir si la fonction gagner marche
##plateau_test = [[1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]


def jouer (table):
    ## Je demande quelle pion le joueur veut déplacer et à quelle endroit
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))
    colonne_depart = int(input("Quelle est sa colonne ?"))
    ligne_arriver = int(input("Vers quelle ligne ?"))
    colonne_arriver = int(input("Vers quelle colonne ?"))
    table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
    table[ligne_depart][colonne_depart] = 0
    print(table)

def gagner (table):
    compteur_1=0
    compteur_2=0
    for i in range (len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1 :
                compteur_1 += 1
            if table[i][j] == 2 :
                compteur_2 += 1
    if compteur_1 == 0:
        print("La joueur 2 a gagné !")
        True
    elif compteur_2 == 0:
        print("La joueur 1 a gagné !")
        True
    else :
        False

while gagner (plateau_test) == False:
    jouer(plateau_test)


plateau_test = [[1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
