from Generation import generer_graphe
from Solution import valider_solution, methode_maison, dfs_backtracking
from Outils import position_vers_nom, nom_vers_position
from Affichage import Echiquier

hauteur = 5
largeur = 5
graph = generer_graphe(hauteur, largeur)
depart = (0, 0)

# solution = dfs_backtracking(graph, position_vers_nom(depart))
solution = methode_maison(graph, position_vers_nom(depart))
valider_solution([nom_vers_position(n) for n in solution], hauteur, largeur)

affichage = Echiquier(hauteur, largeur)
affichage.afficher_solution([nom_vers_position(n) for n in solution])
while affichage.continuer:
    affichage.mettre_a_jour()
