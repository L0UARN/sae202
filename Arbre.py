class Noeud:
    def __init__(self, nom: str) -> None:
        """ Initalise un nouveau noeud.

        :param nom: Le titre du noeud.
        """
        self.nom = nom
        self.parent: Noeud = None
        self.enfants: list[Noeud] = []

    def ajouter(self, enfant: object) -> None:
        """ Permet d'ajouter un nouvel enfant au noeud.

        :param enfant: Un noeud à ajouter aux enfants.
        """
        enfant.parent = self
        self.enfants.append(enfant)

    def comprend(self, nom: str) -> bool:
        """ Permet de savoir si ce noeud contient un enfant portant le nom spécifié.

        :param nom: Le nom du noeud qu'on cherche.
        :return: `True` si un noeud ayant un nom correspondant est trouvé, `False` sinon.
        """
        resultat = False
        noms = [n.nom for n in self.enfants]

        for test in noms:
            if test == nom:
                resultat = True

        return resultat

    def enfant_avec_nom(self, nom: str) -> object:
        """ Permet d'obtenir l'enfant du nœud ayant un nom donné.

        :param nom: Le nom de l'enfant recherché.
        :return: Le nœud enfant du nœud ayant le nom spécifié.
        """
        resultat: Noeud = None

        for enfant in self.enfants:
            if enfant.nom == nom:
                resultat = enfant

        return resultat

    def dernier_enfant(self) -> object:
        """ Permet d'obtenir le dernier enfant ajouté au noeud.

        :return: Le dernier enfant du noeud, ou `None` si le noeud n'a pas d'enfant.
        """
        resultat = None

        if self.enfants:
            resultat = self.enfants[-1]

        return resultat

    def dernier_chemin(self) -> list[str]:
        """ Permet de retourner une liste représentant le chemin qu'il faut prendre pour arriver au dernier noeud ajouté
        à l'arbre.

        :return: La liste des noms des noeuds représentant le chemin.
        """
        resultat: list[str] = [self.nom]

        etape: Noeud = self
        while etape.dernier_enfant() is not None:
            etape = etape.dernier_enfant()
            resultat.append(etape.nom)

        return resultat

    def chemin_jusque_la(self) -> list[str]:
        resultat: list[str] = [self.nom]

        parent = self.parent
        while parent is not None:
            resultat.append(parent.nom)
            parent = parent.parent

        return resultat

    def noms_enfants(self) -> list[str]:
        """ Permet d'obtenir une liste des noms des enfants du noeud.

        :return: La liste des noms de tous les enfants du noeud.
        """
        return [n.nom for n in self.enfants]

    def _afficher(self, decalage: int = 0) -> None:
        """ Permet d'afficher l'arbre dans la console. Utilisé seulement pour debug.

        :param decalage: Ne pas utiliser. Décale avec des '-' l'affichage de l'arbre.
        """
        print(f'{decalage * "-"}{self.nom}')
        for enfant in self.enfants:
            enfant._afficher(decalage=decalage + 1)
