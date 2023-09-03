# Configurations for the game

# Tile/Window size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
TILESIZE = 32

FPS = 60

# Layers for sprites
PLAYER_LAYER = 4
GHOST_LAYER = 3
DOT_LAYER = 2
BLOCK_LAYER = 1

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Dimensions of the grid
TM_X = 20
TM_Y = 20

SPEED = 3  # Speed of the player

# Tilemap for each level
TILEMAP = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W........W.........W",
    "W.WW.WWW.W.WWWW.WW.W",
    "W..................W",
    "W.WW.W.WWWWW.W.WWW.W",
    "W....W...W.........W",
    "WWWW.WWW.W.WWWWWWWWW",
    "WWWW...........WWWWW",
    "WWWW.WWWW-WWWW.WWWWW",
    "W....WI.B.P.CW.....W",
    "W.WWWWWWWWWWWWWWWW.W",
    "W.WWW..........WWW.W",
    "W.....WWWWWWWW.....W",
    "WWWWW....U.....WWWWW",
    "W.....WWWWWWWW.....W",
    "W.WWWW...W....WWWW.W",
    "W.WWWW.W.W.WW.WWWW.W",
    "W.WWWW.W.W.WW.WWWW.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

TILEMAP_2 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W....WWW...WWWW....W",
    "W.WW.WWW.W.WWWW.WW.W",
    "W.WW.W...W......WW.W",
    "W.WW.W.WWWWW.W.WWW.W",
    "W....W...W...W.....W",
    "WWWW.WW.WWWWWW.WWWWW",
    "WWWW...........WWWWW",
    "WWWW.WWWW-WWWW.WWWWW",
    "W....WI.B.P.CW.....W",
    "W.WW.WWWWWWWWW.WWW.W",
    "W.WW...........WWW.W",
    "W.....W.W.W.WW.....W",
    "WW.WW....U.....WW.WW",
    "W.....WWWWWWWW.....W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

TILEMAP_3 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W..................W",
    "W.W.WWWWWW.WWWWw.W.W",
    "W.w..............w.W",
    "W.W.WWWWWW.WWWwW.W.W",
    "W....W.......W.....W",
    "WW.W.WW.WW.WWW.WW.WW",
    "WW................WW",
    "WWWW.WWWW-WWWW.WWWWW",
    "WW...WI.B.P.CW....WW",
    "W..W.WWWWWWWWW.WW..W",
    "W.WW...........WWW.W",
    "W.....WWWW.WWW.....W",
    "WW.WW.W..U..W..WW.WW",
    "W.....WWWW.WWW.....W",
    "W.W................W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

TILEMAP_4 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W.........U........W",
    "WWWWW.WWWWWWWW.WWWWW",
    "W.........W........W",
    "W.WWWWWWW.W.WWwWWW.W",
    "W.WW.WW.W...W.W.WW.W",
    "W.WW.WW.WWWWW.W.WW.W",
    "W..................W",
    "WWWW.WWWW-WWWW.WWWWW",
    "WW...WI.B.P.CW....WW",
    "W..W.WWWWWWWWW.WW..W",
    "W.WW...........WWW.W",
    "W.....WWWWWWWW.....W",
    "W..WWWWWWWWWWWWWW..W",
    "W.....WWWWWWWW.....W",
    "W........W.........W",
    "W.WWWWWW.W.WWWWWWW.W",
    "W......W.W.W.......W",
    "WWWWWW.......WWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
]

TILEMAP_5 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W.........U........W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W....WWWW-WWWW.....W",
    "W....WI.B.P.CW.....W",
    "W....WWWWWWWWW.....W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

# Walls for each level
WALLS = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W........W.........W",
    "W.WW.WWW.W.WWWW.WW.W",
    "W..................W",
    "W.WW.W.WWWWW.W.WWW.W",
    "W....W...W.........W",
    "WWWW.WWW.W.WWWWWWWWW",
    "WWWW...........WWWWW",
    "WWWW.WWWW.WWWW.WWWWW",
    "W....W.......W.....W",
    "W.WWWWWWWWWWWWWWWW.W",
    "W.WWW..........WWW.W",
    "W.....WWWWWWWW.....W",
    "WWWWW..........WWWWW",
    "W.....WWWWWWWW.....W",
    "W.WWWW...W....WWWW.W",
    "W.WWWW.W.W.WW.WWWW.W",
    "W.WWWW.W.W.WW.WWWW.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

WALLS_2 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W....WWW...WWWW....W",
    "W.WW.WWW.W.WWWW.WW.W",
    "W.WW.W...W......WW.W",
    "W.WW.W.WWWWW.W.WWW.W",
    "W....W...W...W.....W",
    "WWWW.WW.WWWWWW.WWWWW",
    "WWWW...........WWWWW",
    "WWWW.WWWW-WWWW.WWWWW",
    "W....W.......W.....W",
    "W.WW.WWWWWWWWW.WWW.W",
    "W.WW...........WWW.W",
    "W.....W.W.W.WW.....W",
    "WW.WW..........WW.WW",
    "W.....WWWWWWWW.....W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

WALLS_3 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W..................W",
    "W.W.WWWWWW.WWWWw.W.W",
    "W.w..............w.W",
    "W.W.WWWWWW.WWWwW.W.W",
    "W....W.......W.....W",
    "WW.W.WW.WW.WWW.WW.WW",
    "WW................WW",
    "WWWW.WWWW-WWWW.WWWWW",
    "WW...W.......W....WW",
    "W..W.WWWWWWWWW.WW..W",
    "W.WW...........WWW.W",
    "W.....WWWW.WWW.....W",
    "WW.WW.W.....W..WW.WW",
    "W.....WWWW.WWW.....W",
    "W.W................W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W.W.WW.W.W.WW.WW.W.W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]

WALLS_4 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W.........U........W",
    "WWWWW.WWWWWWWW.WWWWW",
    "W.........W........W",
    "W.WWWWWWW.W.WWwWWW.W",
    "W.WW.WW.W...W.W.WW.W",
    "W.WW.WW.WWWWW.W.WW.W",
    "W..................W",
    "WWWW.WWWW-WWWW.WWWWW",
    "WW...W.......W....WW",
    "W..W.WWWWWWWWW.WW..W",
    "W.WW...........WWW.W",
    "W.....WWWWWWWW.....W",
    "W..WWWWWWWWWWWWWW..W",
    "W.....WWWWWWWW.....W",
    "W........W.........W",
    "W.WWWWWW.W.WWWWWWW.W",
    "W......W.W.W.......W",
    "WWWWWW.......WWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
]

WALLS_5 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W....WWWW-WWWW.....W",
    "W....W.......W.....W",
    "W....WWWWWWWWW.....W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "W..................W",
    "WWWWWWWWWWWWWWWWWWWW",
]
