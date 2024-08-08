import os

# Konstanta velikosti okna a šachovnice
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB barvy
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Cesty ke zvukovým souborům
SOUND_MOVE = os.path.join('sounds', 'move.mp3')
SOUND_JUMP = os.path.join('sounds', 'jump.mp3')
SOUND_WIN = os.path.join('sounds', 'win.mp3')
