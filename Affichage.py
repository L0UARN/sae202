import pygame as pg
from time import time
from math import floor


def courbe_x(x):
    return -2 / (x - 2) - 1


def courbe_y(x):
    return -2 / (x + 1) + 2


class Echiquier:
    def __init__(self, hauteur: int, largeur: int) -> None:
        """
        :param hauteur: La hauteur de l'échiquier.
        :param largeur: La largeur de l'échiquier.
        """
        pg.init()
        self.fenetre = pg.display.set_mode((800, 800))
        self.continuer = True
        self.debut_affichage = 0
        self.solution: list[tuple[int]] = []
        self.hauteur = hauteur
        self.largeur = largeur
        self.unite_x = 800 // self.largeur
        self.unite_y = 800 // self.hauteur
        self.image = pg.transform.scale(pg.image.load("cavalier.png"), (self.unite_x * 0.75, self.unite_y * 0.75))

    def mettre_a_jour(self) -> None:
        """ Met à jour l'affichage de l'échiquier et dessine le chemin solution s'il est donné.
        """
        for y in range(self.hauteur):
            for x in range(self.largeur):
                couleur = (255, 255, 255) if x % 2 == y % 2 else (0, 0, 0)
                pg.draw.rect(self.fenetre, couleur, pg.Rect(x * self.unite_x, y * self.unite_y, self.unite_x, self.unite_y))

        if self.solution:
            progres = time() - self.debut_affichage
            duree_etape = 0.5
            duree_totale = len(self.solution) * duree_etape
            quantite_affichee = (progres / duree_totale) * len(self.solution) if progres < duree_totale else len(self.solution)

            for i in range(floor(quantite_affichee) - 1):
                debut = (self.solution[i][0] * self.unite_x + self.unite_x // 2), (self.solution[i][1] * self.unite_y + self.unite_y // 2)
                fin = (self.solution[i + 1][0] * self.unite_x + self.unite_x // 2), (self.solution[i + 1][1] * self.unite_y + self.unite_y // 2)
                pg.draw.line(self.fenetre, (255, 192, 0), debut, fin, width=4)
                pg.draw.circle(self.fenetre, (128, 128, 128), fin, self.unite_x // 16)

                if i == 0:
                    pg.draw.circle(self.fenetre, (0, 255, 0), debut, self.unite_x // 4)
                elif i == len(self.solution) - 2:
                    self.fenetre.blit(self.image, (fin[0] - self.unite_y / 4, fin[1] - self.unite_y / 4))

            if quantite_affichee % 1 >= 0.5 and floor(quantite_affichee) > 0:
                deplacement = quantite_affichee % 1

                dernier = (
                    (self.solution[floor(quantite_affichee - 1)][0] * self.unite_x + self.unite_x // 2),
                    (self.solution[floor(quantite_affichee - 1)][1] * self.unite_y + self.unite_y // 2)
                )

                prochain = (
                    (self.solution[floor(quantite_affichee)][0] * self.unite_x + self.unite_x // 2),
                    (self.solution[floor(quantite_affichee)][1] * self.unite_y + self.unite_y // 2)
                )

                intermediaire = (
                    dernier[0] + (prochain[0] - dernier[0]) * courbe_x((deplacement - 0.5) * 2),
                    dernier[1] + (prochain[1] - dernier[1]) * courbe_y((deplacement - 0.5) * 2)
                )

                pg.draw.line(self.fenetre, (255, 192, 0), dernier, intermediaire, width=4)
                self.fenetre.blit(self.image, (intermediaire[0] - self.unite_y / 4, intermediaire[1] - self.unite_y / 4))
            else:
                self.fenetre.blit(self.image, (self.solution[floor(quantite_affichee) - 1][0] * self.unite_x + self.unite_x * 0.25, self.solution[floor(quantite_affichee) - 1][1] * self.unite_y + self.unite_y * 0.25))

        pg.display.update()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.continuer = False
                pg.quit()

    def afficher_solution(self, solution: list[tuple[int, int]]) -> None:
        """ Permet d'indiquer le chemin solution à afficher.

        :param solution: Le chemin à représenter sur l'affichage de l'échiquier.
        """
        self.solution = solution
        self.debut_affichage = time()
