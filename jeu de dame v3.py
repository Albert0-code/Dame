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


def jouer (table,nb_joueur):
	## Je demande quelle pion le joueur veut déplacer et à quelle endroit
	ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?"))
	colonne_depart = int(input("Quelle est sa colonne ?"))
	ligne_arriver = int(input("Vers quelle ligne ?"))
	colonne_arriver = int(input("Vers quelle colonne ?"))
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
	  	print(table)

def gagner (table):
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
				True
			else :
				False

def dame(table):
    "fonction qui permet de trasformer les pions qui arrivent a l'autre bout du plateau en dames."
    for j in range(len(table)):
        if table[0][j] == 2:
            table[0][j] = 4
    for j in range(len(table)):
        if table[9][j] == 1:
            table[9][j] = 3
		

while gagner(plateau) == False:
	jouer(plateau)
	dame(plateau)





