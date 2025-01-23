def initialisation(ligne,colonne,ligne_occupee):
    plateau = []
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

