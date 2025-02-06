#################################################################################
#                                                                                                               Jeu de dame                                                                                                                                                        #
#################################################################################

'Bienvenue dans une nouvelle partie de jeu de dame'


plateau = []

def initialisation(ligne : int ,colonne : int ,ligne_occupee : int):
    """Fonction qui prend en argument un nombre de ligne, de colonne et de ligne
    occupée par chaque camp au debut de la partie et qui créer le plateau de jeu."""
    for i in range(ligne):
        plateau.append([])
        for j in range(colonne):
            plateau[i].append(0)
    for i in range(ligne):
        for j in range(i % 2, colonne, 2):
            if i < ligne_occupee:
                plateau[i][j] = 1
            elif i > ligne-ligne_occupee-1:
                plateau[i][j] = 2
    return plateau


def jouer (table : list):
	"""Fonction qui prend en argument le plateau et qui permet de jouer"""
    voir(table)
	nb_joueur = int(input("Quelle est votre numéro de joueur ?"))
    "Je demande quelle pion le joueur veut déplacer et à quelle endroit"
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
    colonne_depart = int(input("Quelle est sa colonne ?"))-1
    verification(table,nb_joueur,ligne_depart,colonne_depart)
    if manger(table,nb_joueur,ligne_depart,colonne_depart) != True :
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
        table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
        table[ligne_depart][colonne_depart] = 0
        voir(table)
    else :
        voir(table)


def gagner(table : list)
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

def dame(table : list):
    "Cette fonction permet de transformer les pions qui arrivent a l'autre bout du plateau en dames"
    for j in range(len(table)):
        if table[0][j] == 2:
            table[0][j] = 4
            print("Votre pion s'est transformé en dame")
            voir(table)
    for j in range(len(table)):
        if table[len(table)-1][j] == 1:
            table[len(table)-1][j] = 3
            print("Votre pion s'est transformé en dame")
            voir(table)

##def super_dame(table : list):
##    "Cette fonction permet de transformer les dames d'un même joueur qui se rencontrent en super dame"
##    "Elles peuvent se déplacer dans toutes les directions."
##    for j in range(len(table)):
##        if table[0][j] == 2:
##            table[0][j] = 4
##    for j in range(len(table)):
##        if table[9][j] == 1:
##            table[9][j] = 3

def voir(table : list):
    "Cette fonction permet d'écrire le plateau de jeu avec un retour à la ligne à chaque fin de ligne"
    for i in range (len(table)):
        print(table[i])

def verification(table : list,nb_joueur : int,ligne : int,colonne: int):
    "Cette fonction vérifie si le joueur n'essaie pas de déplacer le pion d'un autre joueur ou qu'il n'y a pas de pion sur la case"
    while nb_joueur + 2 != table[ligne][colonne] or nb_joueur != table[ligne][colonne]:
        print("""Vous ne pouvez pas déplacer un pion de votre adversaire ou la case 
        que vous avez donnez est vide""")
        ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
        colonne_depart = int(input("Quelle est sa colonne ?"))-1
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
        

def manger(table : list,nb_joueur : int,ligne_depart : int,colonne_depart : int):
    if nb_joueur == 1 :
        if table[ligne_depart+1][colonne_depart+1] == 2 :
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart+2][colonne_depart+2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart+1][colonne_depart+1] = 0
            return True
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
            return True
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

##"Test pour savoir si la fonction manger marche"
##plateau_test1 = [[1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [0,0,2,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]
##
##while gagner(plateau_test1) == False:
##	jouer(plateau_test1)

"Test pour savoir si la fonction dame marche"
plateau_test1 = [[1,0,1,0,1,0,1,0,1,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,2,0,0,0,0,0,3,0],
           [0,0,0,0,0,0,0,0,0,0]]

while gagner(plateau_test1) == False:
	jouer(plateau_test1)
	dame(plateau_test1)
	super_dame(plateau_test1)





