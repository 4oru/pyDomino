import pygame

class DominoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, window):
        # Dibuja las fichas del jugador en una posición específica en la ventana
        x = 100  # Ejemplo: posición x de las fichas del jugador
        y = 400  # Ejemplo: posición y de las fichas del jugador
        for tile in self.hand:
            tile.draw(window, x, y)
            x += tile_width + 10  # Espacio entre fichas
