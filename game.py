import pygame
import json
from constants import RED, WHITE, SQUARE_SIZE, SOUND_MOVE, SOUND_JUMP, SOUND_WIN
from board import Board

pygame.mixer.init()
sound_move = pygame.mixer.Sound(SOUND_MOVE)
sound_jump = pygame.mixer.Sound(SOUND_JUMP)
sound_win = pygame.mixer.Sound(SOUND_WIN)

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            skipped = self.valid_moves[(row, col)]
            self.board.move(self.selected, row, col)
            if skipped:
                self.board.remove(skipped)
                sound_jump.play()  # Přehrajte zvuk skoku
                self.valid_moves = self.board.get_valid_moves(self.selected)
                if not self.valid_moves:
                    self.change_turn()
                else:
                    return True
            else:
                sound_move.play()  # Přehrajte zvuk pohybu
                self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, (0, 255, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def save_game(self, filename='savegame.json'):
        game_state = {
            'board': self.board.board,
            'turn': self.turn,
            'selected': (self.selected.row, self.selected.col) if self.selected else None
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f)

    def load_game(self, filename='savegame.json'):
        with open(filename, 'r') as f:
            game_state = json.load(f)

        self.board.board = game_state['board']
        self.turn = game_state['turn']
        if game_state['selected']:
            self.selected = self.board.get_piece(*game_state['selected'])
        else:
            self.selected = None
        self.valid_moves = {}

    def check_winner(self):
        winner = self.board.winner()
        if winner is not None:
            sound_win.play()  # Přehrajte zvuk vítězství
            return winner
        return None
