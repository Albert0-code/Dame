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

### Test pour savoir si la fonction gagner marche
##plateau_test = [[1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [1,0,1,0,1,0,1,0,1,0],
##           [0,1,0,1,0,1,0,1,0,1],
##           [0,0,0,0,0,0,0,0,0,0],
##           [0,0,0,0,0,0,0,0,0,0]]

### Test de la fonction gagner sur le plateau test
##while gagner (plateau_test) == False:
	##jouer(plateau_test)


def jouer (table):
    voir(table)
    nb_joueur = int(input("Quelle est votre numéro de joueur ?"))
    ## Je demande quelle pion le joueur veut déplacer et à quelle endroit
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
    colonne_depart = int(input("Quelle est sa colonne ?"))-1
    ligne_arriver = int(input("Vers quelle ligne ?"))-1
    colonne_arriver = int(input("Vers quelle colonne ?"))-1
    verification(table,nb_joueur,ligne_depart,colonne_depart)
    if nb_joueur == 1 and table[ligne_arriver][colonne_arriver] == 2 :
	    table[ligne_arriver][colonne_arriver] = 0
	    if colonne_arriver > colonne_depart :
		    table[ligne_arriver+1][colonne_arriver+1] = 1
	    else :
		    table[ligne_arriver+1][colonne_arriver-2] = 1
    elif nb_joueur == 2 and table[ligne_arriver][colonne_arriver] == 1 :
	    table[ligne_arriver][colonne_arriver] = 0
	    if colonne_arriver > colonne_depart :
		    table[ligne_arriver-1][colonne_arriver+1] = 2
	    else :
		    table[ligne_arriver-1][colonne_arriver-2] = 2
    else :
        table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
        table[ligne_depart][colonne_depart] = 0

def gagner(table):
    "fonction qui permet de mettre fin à la partie quand un joueur n'a plus de pions en jeu."
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
    "fonction qui permet de trasformer les pions qui arrivent a l'autre bout du plateau en dames."
    for j in range(len(table)):
        if table[0][j] == 2:
            table[0][j] = 4
    for j in range(len(table)):
        if table[9][j] == 1:
            table[9][j] = 3

def voir(table):
    for i in range (len(table)):
        print(table[i])

def verification(table,nb_joueur,ligne,colonne):
    while nb_joueur != table[ligne][colonne]:
        print("Vous ne pouvez pas déplacer un pion de votre adversaire")
        ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))-1
        colonne_depart = int(input("Quelle est sa colonne ?"))-1
        ligne_arriver = int(input("Vers quelle ligne ?"))-1
        colonne_arriver = int(input("Vers quelle colonne ?"))-1
		

while gagner(plateau) == False:
    jouer(plateau)
    dame(plateau)





