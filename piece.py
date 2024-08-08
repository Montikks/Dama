import pygame
from constants import RED, WHITE, SQUARE_SIZE, GREY, ROWS


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(win, GREY, (self.x, self.y), radius // 2)

    def draw_at(self, win, x, y):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (x, y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (x, y), radius)
        if self.king:
            pygame.draw.circle(win, GREY, (x, y), radius // 2)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        if (self.color == WHITE and self.row == 0) or (self.color == RED and self.row == ROWS - 1):
            self.make_king()

    def __repr__(self):
        return str(self.color)
