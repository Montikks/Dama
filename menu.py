import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE

class Menu:
    def __init__(self, win):
        self.win = win
        self.font = pygame.font.Font(None, 74)

    def draw(self):
        self.win.fill((0, 0, 0))
        title = self.font.render('Dáma', True, (255, 255, 255))
        start_button = self.font.render('Start', True, (255, 255, 255))
        self.win.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
        self.win.blit(start_button, (WIDTH // 2 - start_button.get_width() // 2, HEIGHT // 2))
        pygame.display.update()

    def get_click(self, pos):
        x, y = pos
        if WIDTH // 2 - 50 <= x <= WIDTH // 2 + 50 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
            return 'start'
        return None
