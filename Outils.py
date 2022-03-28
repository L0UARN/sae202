def liste_moins(l1: list[str], l2: list[str]) -> list[str]:
    """ Permet de soustraire le contenu d'une liste à une autre.

    :param l1: La liste dont le contenu va être soustrait.
    :param l2: La liste qui soustrait l'autre liste.
    :return: La liste `l1`, ne contenant plus ses éléments communs à `l2`.
    """
    return [e for e in l1 if e not in l2]


def nom_vers_position(nom: str) -> tuple[int, int]:
    """ Permet de convertir un 'nom' (une position sous forme de chaîne de caractères)

    :param nom: La position à convertir en tuple
    :return: La position sous forme de tuple
    """
    bouts = nom.split(';')
    return int(bouts[0]), int(bouts[1])


def position_vers_nom(position: tuple[int, int]) -> str:
    """ Permet de convertir une position en un 'nom' (une position sous forme de chaîne de caractères)

    :param position: La position à convertir en chaîne de caractères
    :return: La position sous forme de chaîne de caractères
    """
    return f'{position[0]};{position[1]}'
