import pygame
from domino_game import DominoGame

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Dominó")
clock = pygame.time.Clock()

def main():
    game = DominoGame(window)
    game.run()

if __name__ == "__main__":
    main()
