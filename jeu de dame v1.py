def initialisation ():
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
    ligne_depart = int(input("Quelle est la ligne du pion que vous voulez déplacer ?")
    colonne_depart = int(input("Quelle est sa colonne ?")
    ligne_arriver = int(input("Vers quelle ligne ?")
    colonne_arriver = int(input("Vers quelle colonne ?")
    table[ligne_arriver][colonne_arriver] = table[ligne_depart][colonne_depart]
    table[ligne_depart][colonne_depart] = 0
    print(table)

jouer(plateau)

            
