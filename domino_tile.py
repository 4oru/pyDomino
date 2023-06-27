import pygame

class DominoTile:
    def __init__(self, number_left, number_right):
        self.number_left = number_left
        self.number_right = number_right
        self.rect = pygame.Rect(0, 0, tile_width, tile_height)

    def draw(self, window, x, y):
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(window, (255, 255, 255), self.rect)
        number_font = pygame.font.SysFont(None, 30)
        number_left_text = number_font.render(str(self.number_left), True, (0, 0, 0))
        number_right_text = number_font.render(str(self.number_right), True, (0, 0, 0))
        window.blit(number_left_text, (self.rect.x + 10, self.rect.y + 10))
        window.blit(number_right_text, (self.rect.x + tile_width - 30, self.rect.y + tile_height - 30))
