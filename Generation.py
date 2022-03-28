from Outils import position_vers_nom


def position_valide(position: tuple[int, int], hauteur: int, largeur: int) -> bool:
    """ Vérifie si une position fait partie d'un échiquier d'une taille donnée

    :param position: La position dont on veut vérifier la validité
    :param taille: La taille de l'échiquier (son côté)
    :return: `True` si la position est valide, `False` sinon
    """
    return 0 <= position[0] < largeur and 0 <= position[1] < hauteur


def prochaines_positions(position: tuple[int, int], hauteur: int, largeur: int) -> list[tuple[int, int]]:
    """ Retourne une liste de tous les déplacements possible d'un cavalier à partir d'une case

    :param position: La position actuelle du cavalier
    :param taille: La taille de l'échiquier (son côté)
    :return: La liste de toutes les positions que peut prendre le cavalier à partir de sa position actuelle
    """
    prochaines: list[tuple[int, int]] = []

    if position_valide((position[0] - 2, position[1] - 1), hauteur, largeur):
        prochaines.append((position[0] - 2, position[1] - 1))
    if position_valide((position[0] - 1, position[1] - 2), hauteur, largeur):
        prochaines.append((position[0] - 1, position[1] - 2))
    if position_valide((position[0] + 2, position[1] - 1), hauteur, largeur):
        prochaines.append((position[0] + 2, position[1] - 1))
    if position_valide((position[0] + 1, position[1] - 2), hauteur, largeur):
        prochaines.append((position[0] + 1, position[1] - 2))
    if position_valide((position[0] - 2, position[1] + 1), hauteur, largeur):
        prochaines.append((position[0] - 2, position[1] + 1))
    if position_valide((position[0] - 1, position[1] + 2), hauteur, largeur):
        prochaines.append((position[0] - 1, position[1] + 2))
    if position_valide((position[0] + 2, position[1] + 1), hauteur, largeur):
        prochaines.append((position[0] + 2, position[1] + 1))
    if position_valide((position[0] + 1, position[1] + 2), hauteur, largeur):
        prochaines.append((position[0] + 1, position[1] + 2))

    return prochaines


def generer_graphe(hauteur: int, largeur: int) -> dict[str, list[str]]:
    """ Retourne un graphe des déplacements possible d'un cavalier sur un échiquier d'une taille donnée

    :param taille: La taille de l'échiquier (son côté)
    :return: Un graphe représentant les déplacements possibles d'un cavalier
    """
    graphe: dict[str, list[str]] = {}

    for y in range(0, hauteur):
        for x in range(0, largeur):
            graphe[position_vers_nom((x, y))] = [position_vers_nom(p) for p in prochaines_positions((x, y), hauteur, largeur)]

    return graphe
