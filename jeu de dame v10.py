#################################################################################
#                                                                                                               Jeu de dame                                                                                                                                                        #
#################################################################################

'Bienvenue dans une nouvelle partie de jeu de dame'
'Le jeu de dames se joue sur un plateau de 10x10 cases, chaque joueur disposant de 20 pièces placées sur les cases noires des quatre premières rangées'
'Le but du jeu est de capturer toutes les pièces adverses ou de les empêcher de jouer'
'Les pièces se déplacent en diagonale, d une seule case à la fois'
'Lorsqu une pièce se trouve devant une pièce adverse, elle peut sauter par-dessus celle-ci pour la capturer, à condition que la case suivante soit vide'
'Le saut est obligatoire lorsqu il est possible, et un joueur peut effectuer plusieurs sauts dans un même tour, tant que chaque saut respecte les règles'
'Lorsqu une pièce atteint la dernière rangée du côté adverse, elle est promue en dame'
'La dame a la capacité de se déplacer sur plusieurs cases à la fois, toujours en diagonale, et peut sauter par-dessus plusieurs pièces dans une seule prise'
'Le jeu se termine lorsqu un joueur capture toutes les pièces adverses ou bloque l adversaire de manière à ce qu il ne puisse plus jouer'
'Si aucune des deux situations ne se produit, la partie peut être déclarée nulle'

plateau = []

def initialisation(ligne : int ,colonne : int ,ligne_occupee : int):
    """Fonction qui prend en argument un nombre de ligne, de colonne et de ligne
    occupée par chaque camp au debut de la partie et qui créer le plateau de jeu."""
    while ligne/2 < ligne_occupee :
        ligne_occupee=int(input('Veuillez choisir un nombre de ligne valide '))
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
    "Fonction qui prend en argument le plateau et qui permet de jouer"
    voir(table)
    nb_joueur = int(input("Quelle est votre numéro de joueur ?"))
    "Je demande quelle pion le joueur veut déplacer et à quelle endroit"
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
    colonne_depart = int(input("Quelle est sa colonne ?"))-1
    #verification(table,nb_joueur,ligne_depart,colonne_depart)
    if manger(table,nb_joueur,ligne_depart,colonne_depart) != True :
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
        if super_dame(table,nb_joueur,ligne_depart,colonne_depart,ligne_arriver,colonne_arriver) == True :
            table[ligne_arriver][colonne_arriver] = nb_joueur + 2
            table[ligne_depart][colonne_depart] = 0
        else :
            table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
            table[ligne_depart][colonne_depart] = 0
    dame(plateau_test1)
    voir(table)


def gagner(table : list):
    """Fonction qui prend en argument le plateau et qui permet de
    mettre fin à la partie quand un joueur n'a plus de pions en jeu."""
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
    """Fonctionqui prend en argument le plateau et qui permet de transformer
    les pions qui arrivent a l'autre bout du plateau en dames"""
    for j in range(len(table)):
        if table[0][j] == 2:
            table[0][j] = 4
            print("Votre pion s'est transformé en dame")
    for j in range(len(table)):
        if table[len(table)-1][j] == 1:
            table[len(table)-1][j] = 3
            print("Votre pion s'est transformé en dame")

def super_dame(table : list,nb_joueur : int,ligne_depart : int,colonne_depart : int,\
               ligne_arriver : int,colonne_arriver : int):
    "Cette fonction permet de transformer les dames d'un même joueur qui se rencontrent en super dame"
    "Elles peuvent se déplacer dans toutes les directions."
    if table[ligne_arriver][colonne_arriver] == table[ligne_depart][colonne_depart] == nb_joueur + 2:
        return True
    else :
        return False

def voir(table : list):
    """Fonction qui prend en argument le plateau et qui permet d'afficher
    le plateau de jeu avec un retour à la ligne à chaque fin de ligne"""
    for i in range (len(table)):
        print(table[i])

def verification(table : list,nb_joueur : int,ligne : int,colonne: int):
    """Fonction qui prend en argument le plateau, le numéro du joueur et le coup qui va etre joue
    et qui vérifie si le joueur n'essaie pas de déplacer le pion d'un autre joueur
    ou qu'il n'y a pas de pion sur la case"""
    while nb_joueur != table[ligne][colonne]:
        print("""Vous ne pouvez pas déplacer un pion de votre adversaire ou la case 
        que vous avez donnez est vide""")
        ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
        colonne_depart = int(input("Quelle est sa colonne ?"))-1
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
        

def manger(table : list,nb_joueur : int,ligne_depart : int,colonne_depart : int):
    """Fonction qui prend en argument le tableau, le numero du joueur et la position du pion qui veut etre joue
    et qui nous dit si on doit manger un pion de l'adversaire au lieu de jouer ce coup."""
    if nb_joueur == 1 or table[ligne_depart][colonne_depart] == 3:
        if table[ligne_depart+1][colonne_depart+1] == 2 or table[ligne_depart+1][colonne_depart+1] == 4:                
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart+2][colonne_depart+2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart+1][colonne_depart+1] = 0
            return True
        elif table[ligne_depart+1][colonne_depart-1] == 2 or table[ligne_depart+1][colonne_depart+1] == 4:
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart+2][colonne_depart-2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart+1][colonne_depart-1] = 0
            return True
    elif nb_joueur == 2 or table[ligne_depart][colonne_depart] == 4:
        if table[ligne_depart-1][colonne_depart+1] == 1 or table[ligne_depart+1][colonne_depart+1] == 3:
            print("Vous devez mangé un pion de l'adversaire")
            table[ligne_depart-2][colonne_depart+2] = table[ligne_depart][colonne_depart] 
            table[ligne_depart][colonne_depart] = 0
            table[ligne_depart-1][colonne_depart+1] = 0
            return True
        elif table[ligne_depart-1][colonne_depart-1] == 1 or table[ligne_depart+1][colonne_depart+1] == 3:
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

##"Test pour savoir si la fonction dame marche"
##plateau_test1 = [[1,0,1,0,1,0,1,0,1,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,2,0,0,0,0,0,1,0],
##           [0,0,0,0,0,0,0,0,0,0]]
##
##while gagner(plateau_test1) == False:
##	jouer(plateau_test1)

initialisation(int(input('Combien de ligne votre plateau fait-il ?')),\
               int(input('Combien de colonne votre plateau fait-il ?')),\
               int(input('Combien de ligne occupée par joueur a-t-il ?')))
while gagner(plateau) == False:
	jouer(plateau)







