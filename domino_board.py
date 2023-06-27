import pygame

class DominoBoard:
    def __init__(self):
        self.tiles = []

    def draw(self, window):
        window.fill((0, 128, 0))  # Dibuja un fondo verde para el tablero
        for tile in self.tiles:
            tile.draw(window)
