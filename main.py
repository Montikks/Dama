import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, SOUND_MOVE, SOUND_JUMP, SOUND_WIN
from game import Game
from minimax import minimax
from menu import Menu

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dáma')

# Inicializace zvuků
pygame.mixer.init()
sound_move = pygame.mixer.Sound(SOUND_MOVE)
sound_jump = pygame.mixer.Sound(SOUND_JUMP)
sound_win = pygame.mixer.Sound(SOUND_WIN)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    pygame.font.init()  # Inicializace fontů
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    menu = Menu(WIN)

    in_menu = True

    while run:
        clock.tick(60)

        if in_menu:
            menu.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if menu.get_click(pos) == 'start':
                        in_menu = False
        else:
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 3, float('-inf'), float('inf'), True, game)
                game.ai_move(new_board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Klávesová zkratka pro uložení hry
                        game.save_game()
                    if event.key == pygame.K_l:  # Klávesová zkratka pro načtení hry
                        game.load_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            if game.board.winner() is not None:
                print(f"Winner: {game.board.winner()}")
                run = False

            game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
