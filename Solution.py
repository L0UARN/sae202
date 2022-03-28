from Arbre import Noeud
from Outils import liste_moins
from Generation import prochaines_positions


def classement_voisins(graph: dict[str, list[str]], sommet: str, visites: list[str]) -> list[str]:
    """ Permet d'obtenir une liste des voisins d'un sommet, classés de façon à avoir en premier les voisins dont leur
    propre nombre de voisins est minimal. Cela permet d'explorer en premier les voisins les moins accessibles, et ainsi
    trouver plus rapidement une solution au problème.

    :param graph: Le graphe dans lequel on doit chercher les voisins du sommet donné.
    :param sommet: Le sommet dont on doit classer les voisins.
    :param visites: Une liste des sommets déjà visités (à exclure des voisins)
    :return: La liste des voisins du sommet, triée en fonction de leur nombre de voisins.
    """
    resultats: list[tuple[str, int]] = []
    interdits = visites + [sommet]

    for voisin in graph[sommet]:
        if voisin not in interdits:
            resultats.append((voisin, len(liste_moins(graph[voisin], visites))))

    return [r[0] for r in sorted(resultats, key=lambda r: r[1])]


def methode_maison(graph: dict[str, list[str]], depart: str) -> list[str]:
    """ Solution au problème du tour du cavalier. Méthode itérative, utilisant un arbre pour représenter les chemins
    choisis ainsi que pour remonter en cas d'impasse.

    :param graph: Le graph de l'échiquier sur lequel le cavalier se déplace.
    :param depart: Le point de départ du cavalier sur l'échiquier.
    :return: La liste des sommets visités (dans l'ordre), correspondant donc à la solution au problème.
    """
    a_visiter: str = depart
    visites: list[str] = []
    chemins: Noeud = Noeud(depart)
    etape: Noeud = chemins

    while a_visiter is not None:
        sommet = a_visiter
        visites.append(sommet)

        # On ajoute au nœud correspondant à l'étape précédente, le sommet actuel
        if not etape.comprend(sommet):
            etape.ajouter(Noeud(sommet))
        # Et on met à jour l'étape actuelle pour qu'elle corresponde à l'étape actuelle
        etape = etape.enfant_avec_nom(sommet)

        # On visite tous les voisins du sommet actuel
        # (Seulement ceux qui n'ont pas déjà été explorés)
        nouveaux = classement_voisins(graph, a_visiter, visites)

        # Si le sommet actuel a des voisins qui n'ont pas encore été visités
        if nouveaux:
            a_visiter = nouveaux[0]
        # Sinon, ça signifie qu'on est arrivés dans une impasse
        # On est arrivé à une impasse après avoir visité tous les sommets
        elif len(visites) == len(graph):
            a_visiter = None
        # On est arrivé dans une impasse sans passer par tous les sommets
        # Il faut donc retourner en arrière pour trouver un point auquel on peut faire un choix différent
        else:
            # On remonte l'arbre des choix nœud par nœud, jusqu'à trouver un chemin qui n'est pas encore exploré
            # Ou jusqu'à ce qu'on remonte tout en haut de l'arbre, auquel cas on aura exploré tous les chemins possibles
            # et donc déterminé qu'aucune solution n'est possible
            nouveau = etape.parent
            choix = classement_voisins(graph, nouveau.nom, nouveau.chemin_jusque_la() + nouveau.noms_enfants())
            while nouveau is not None and not choix:
                nouveau = nouveau.parent
                choix = classement_voisins(graph, nouveau.nom, nouveau.chemin_jusque_la() + nouveau.noms_enfants())

            # Si on n'est pas remonté jusqu'en haut de l'arbre
            if nouveau is not None:
                # On reprend le chemin à partir du nouveau sommet
                visites = nouveau.chemin_jusque_la()
                a_visiter = choix[0]
                etape = nouveau
            # Sinon, aucune solution n'est possible, alors on quitte
            else:
                break

    return visites


def dfs_backtracking(graph: dict[str, list[str]], depart: str, visites: list[str] = []) -> list[str]:
    """ Solution au problème du tour du cavalier. Méthode récursive.

    :param graph: Le graph de l'échiquier sur lequel le cavalier se déplace.
    :param depart: Le point de départ du cavalier sur l'échiquier.
    :param visites: La liste des sommets visités. Ne pas renseigner lors du premier appel de la fonction.
    :return: La liste des sommets visités (dans l'ordre), correspondant donc à la solution au problème.
    """
    # Si on a visité toutes les cases de l'échiquier
    if len(visites) == len(graph) - 1:
        # Alors on a trouvé une solution au problème, qu'on retourne donc
        return visites + [depart]
    # Sinon, si on se retrouve dans une impasse
    elif len(classement_voisins(graph, depart, visites)) == 0:
        # Alors on retourne une liste vide (indiquant que ce chemin ne mène à rien)
        return []
    # Sinon, c'est qu'on est sur un chemin qui n'a pas fini d'être exploré
    else:
        chemin = []
        # On continue d'explorer tous les voisins du sommet de départ
        for voisin in classement_voisins(graph, depart, visites):
            temp = dfs_backtracking(graph, voisin, visites + [depart])
            # Si le chemin trouvé contient des étapes (n'est pas une liste vide -> est une solution)
            # Alors on retourne ce chemin
            # Sinon, on retourne une liste vide
            if temp:
                chemin = temp
                break

        return chemin


def valider_solution(solution: list[tuple[int, int]], hauteur: int, largeur: int) -> bool:
    """ Permet de valider si une "solution" au problème du tour du cavalier est réellement une solution. Cette fonction
    affiche les trois critères selon lequels une solution est considérée valide : si le chemin passe bien par toutes les
    cases, si chaque étape du chemin est unique, et si tous les déplacements sont légaux.

    :param solution: La proposition de solution.
    :param hauteur: La hauteur de l'échiquier.
    :param largeur: La largeur de l'échiquier.
    :return: `True` si la solution est valide, `False` sinon.
    """
    if not solution:
        print('Aucune solution n\'a été trouvée.')

    taille_correcte: bool = len(solution) == hauteur * largeur

    unique: bool = True
    for i in range(len(solution)):
        unique = unique and (solution[i] not in solution[0:i])

    continu: bool = True
    for i in range(len(solution) - 1):
        continu = continu and (solution[i + 1] in prochaines_positions(solution[i], hauteur, largeur))

    print(f'Taille correcte : {taille_correcte} ({len(solution)} / {hauteur * largeur}).')
    print(f'Étapes uniques : {unique}.')
    print(f'Chemin continu : {continu}.')

    return taille_correcte and unique and continu
