#################################################################################
#                                                                                                               Jeu de dame                                                                                                                                                        #
#################################################################################

'Bienvenue dans une nouvelle partie de jeu de dame'


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


def jouer (table):
    voir(table)
    nb_joueur = int(input("Quelle est votre numéro de joueur ?"))
    ## Je demande quelle pion le joueur veut déplacer et à quelle endroit
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
    colonne_depart = int(input("Quelle est sa colonne ?"))-1
    verification(table,nb_joueur,ligne_depart,colonne_depart)
    if manger(table,nb_joueur,ligne_depart,colonne_depart) == False :
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
        table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
        table[ligne_depart][colonne_depart] = 0
        voir(table)
    else :
        voir(table)


def gagner(table):
    "Cette fonction permet de mettre fin à la partie quand un joueur n'a plus de pions en jeu"
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
        return True
    else :
        return False

def dame(table):
    "Cette fonction permet de transformer les pions qui arrivent a l'autre bout du plateau en dames"
    for j in range(len(table)):
        if table[0][j] == 2:
            table[0][j] = 4
    for j in range(len(table)):
        if table[9][j] == 1:
            table[9][j] = 3

def voir(table):
    "Cette fonction permet d'écrire le plateau de jeu avec un retour à la ligne à chaque fin de ligne"
    for i in range (len(table)):
        print(table[i])

def verification(table,nb_joueur,ligne,colonne):
    "Cette fonction vérifie si le joueur n'essaie pas de déplacer le pion d'un autre joueur ou qu'il n'y a pas de pion sur la case"
    while nb_joueur != table[ligne][colonne]:
        print("Vous ne pouvez pas déplacer un pion de votre adversaire ou la case que vous avez donnez est vide")
        ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
        colonne_depart = int(input("Quelle est sa colonne ?"))-1
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1

def manger(table,nb_joueur,ligne_depart,colonne_depart):
    if nb_joueur == 1 :
        if table[ligne_depart+1][colonne_depart+1] == 2 :
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart+2][colonne_depart+2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart+1][colonne_depart+1] = 0
        elif table[ligne_depart+1][colonne_depart-1] == 2 :
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart+2][colonne_depart-2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart+1][colonne_depart-1] = 0
            return True
    elif nb_joueur == 2 :
        if table[ligne_depart-1][colonne_depart+1] == 1 :
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart-2][colonne_depart+2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart-1][colonne_depart+1] = 0
        elif table[ligne_depart-1][colonne_depart-1] == 2 :
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart-2][colonne_depart-2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart-1][colonne_depart-1] = 0
            return True
    else :
        return False
		

##while gagner(plateau) == False:
##    jouer(plateau)
##    dame(plateau)

##"Test pour savoir si la fonction gagner marche"
##plateau_test = [[1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]

##while gagner (plateau_test) == False:
	##jouer(plateau_test)

"Test pour savoir si la fonction manger marche"
plateau_test1 = [[1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1,0,1],
           [0,0,2,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]

while gagner(plateau_test1) == False:
	jouer(plateau_test1)





