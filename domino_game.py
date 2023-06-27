import pygame
from domino_board import DominoBoard
from domino_player import DominoPlayer

class DominoGame:
    def __init__(self, window):
        self.window = window
        self.board = DominoBoard()
        self.players = [DominoPlayer("Jugador 1"), DominoPlayer("Jugador 2")]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.window.fill((0, 0, 0))
            self.board.draw(self.window)
            for player in self.players:
                player.draw(self.window)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
