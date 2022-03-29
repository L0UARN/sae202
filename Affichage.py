import pygame as pg
from time import time


class Echiquier:
    def __init__(self, hauteur: int, largeur: int) -> None:
        """
        :param hauteur: La hauteur de l'échiquier.
        :param largeur: La largeur de l'échiquier.
        """
        pg.init()
        self.fenetre = pg.display.set_mode((800, 800))
        self.continuer = True
        self.changement = True
        self.debut_affichage = 0
        self.solution: list[tuple[int]] = []
        self.hauteur = hauteur
        self.largeur = largeur

    def mettre_a_jour(self) -> None:
        """ Met à jour l'affichage de l'échiquier et dessine le chemin solution s'il est donné.
        """
        if self.changement:
            progres = (time() - self.debut_affichage) / (len(self.solution) * 0.1)

            unite_x = 800 // self.largeur
            unite_y = 800 // self.hauteur

            for y in range(self.hauteur):
                for x in range(self.largeur):
                    couleur = (255, 255, 255) if x % 2 == y % 2 else (0, 0, 0)
                    pg.draw.rect(self.fenetre, couleur, pg.Rect(x * unite_x, y * unite_y, unite_x, unite_y))

            if self.solution:
                for i in range(int((len(self.solution) - 1) * progres)):
                    debut = (self.solution[i][0] * unite_x + unite_x // 2), (self.solution[i][1] * unite_y + unite_y // 2)
                    fin = (self.solution[i + 1][0] * unite_x + unite_x // 2), (self.solution[i + 1][1] * unite_y + unite_y // 2)
                    pg.draw.line(self.fenetre, (255, 192, 0), debut, fin, width=4)
                    pg.draw.circle(self.fenetre, (128, 128, 128), fin, unite_x // 16)

                    if i == 0:
                        pg.draw.circle(self.fenetre, (0, 255, 0), debut, unite_x // 4)
                    elif i == len(self.solution) - 2:
                        pg.draw.circle(self.fenetre, (255, 0, 0), fin, unite_x // 4)

            pg.display.update()

            if progres >= 1.0:
                self.changement = False

        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.continuer = False
                pg.quit()

    def afficher_solution(self, solution: list[tuple[int, int]]) -> None:
        """ Permet d'indiquer le chemin solution à afficher.

        :param solution: Le chemin à représenter sur l'affichage de l'échiquier.
        """
        self.solution = solution
        self.changement = True
        self.debut_affichage = time()
