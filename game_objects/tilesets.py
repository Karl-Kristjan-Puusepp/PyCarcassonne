from tile_objects.road import Road
from tile_objects.city import City
from tile_objects.field import Field
from tile_objects.monastery import Monastery
from tile_objects.tile import Tile


tile_A = Tile(
    tile_id='A',
    monastery=Monastery(),
    roads=[
        Road(connections=('S', '-'))
    ],
    fields=[
        Field(connections=('NE', 'EN', 'ES', 'SE', 'SW', 'WS', 'WN', 'NW'))
    ])

tile_B = Tile(
    tile_id='B',
    monastery=Monastery(),
    fields=[
        Field(connections=('NE', 'EN', 'ES', 'SE', 'SW', 'WS', 'WN', 'NW'))
    ])

tile_C = Tile(
    tile_id='C',
    cities=[
        City(connections=('N', 'S', 'E', 'W'), has_shield=True)
    ])

tile_D = Tile(  # We don't include starting tile
    tile_id='D',
    cities=[
        City(connections=('E'))
    ],
    roads=[
        Road(connections=('N', 'S'))
    ],
    fields=[
        Field(connections=('NE', 'SE'),
              touching_city=True),
        Field(connections=('NW', 'WN', 'WS', 'SW'))
    ])

tile_E = Tile(
    tile_id='E',
    cities=[
        City(connections=('N'))
    ],
    fields=[
        Field(connections=('EN', 'ES', 'SE', 'SW', 'WS', 'WN'),
              touching_city=True)
    ])

tile_F = Tile(
    tile_id='F',
    cities=[
        City(connections=('W', 'E'),
             has_shield=True)
    ],
    fields=[
        Field(connections=('NE', 'NW'),
              touching_city=True),
        Field(connections=('SE', 'SW'),
              touching_city=True)
    ])

tile_G = Tile(
    tile_id='G',
    cities=[
        City(connections=('N', 'S'))
    ],
    fields=[
        Field(connections=('WN', 'WS'),
              touching_city=True),
        Field(connections=('EN', 'ES'),
              touching_city=True)
    ])

tile_H = Tile(
    tile_id='H',
    cities=[
        City(connections=('E')),
        City(connections=('W'))
    ],
    fields=[
        Field(connections=('NW', 'NE', 'SW', 'SE'),
              touching_city=True)
    ])

tile_I = Tile(
    tile_id='I',
    cities=[
        City(connections=('E')),
        City(connections=('S'))
    ],
    fields=[
        Field(connections=('NW', 'NE', 'WN', 'WS'),
              touching_city=True)
    ])

tile_J = Tile(
    tile_id='J',
    roads=[
        Road(connections=('S', 'E'))
    ],
    cities=[
        City(connections=('N'))
    ],
    fields=[
        Field(connections=('EN', 'WN', 'WS', 'SW'),
              touching_city=True),
        Field(connections=('SE', 'ES'))
    ])

tile_K = Tile(
    tile_id='K',
    roads=[
        Road(connections=('N', 'W'))
    ],
    cities=[
        City(connections=('E'))
    ],
    fields=[
        Field(connections=('NE', 'SE', 'SW', 'WS'),
              touching_city=True),
        Field(connections=('NW', 'WN'))
    ])

tile_L = Tile(
    tile_id='L',
    roads=[
        Road(connections=('N', '-')),
        Road(connections=('S', '-')),
        Road(connections=('W', '-'))
    ],
    cities=[
        City(connections=('E'))
    ],
    fields=[
        Field(connections=('NW', 'WN')),
        Field(connections=('SW', 'WS')),
        Field(connections=('NE', 'SE'),
              touching_city=True)
    ])

tile_M = Tile(
    tile_id='M',
    cities=[
        City(connections=('N', 'W'),
             has_shield=True)
    ],
    fields=[
        Field(connections=('EN', 'ES', 'SE', 'SW'),
              touching_city=True)
    ])

tile_N = Tile(
    tile_id='N',
    cities=[
        City(connections=('N', 'W'))
    ],
    fields=[
        Field(connections=('EN', 'ES', 'SE', 'SW'),
              touching_city=True)
    ])

tile_O = Tile(
    tile_id='O',
    roads=[
        Road(connections=('E', 'S'))
    ],
    cities=[
        City(connections=('N', 'W'),
             has_shield=True)
    ],
    fields=[
        Field(connections=('EN', 'SW'),
              touching_city=True),
        Field(connections=('ES', 'SE'))
    ])

tile_P = Tile(
    tile_id='P',
    roads=[
        Road(connections=('E', 'S'))
    ],
    cities=[
        City(connections=('N', 'W'))
    ],
    fields=[
        Field(connections=('EN', 'SW'),
              touching_city=True),
        Field(connections=('ES', 'SE'))
    ])

tile_Q = Tile(
    tile_id='Q',
    cities=[
        City(connections=('N', 'W', 'E'),
             has_shield=True)
    ],
    fields=[
        Field(connections=('SE', 'SW'),
              touching_city=True),
    ])

tile_R = Tile(
    tile_id='R',
    cities=[
        City(connections=('N', 'W', 'E'))
    ],
    fields=[
        Field(connections=('SE', 'SW'),
              touching_city=True),
    ])

tile_S = Tile(
    tile_id='S',
    roads=[
        Road(connections=('S', '-'))
    ],
    cities=[
        City(connections=('N', 'W', 'E'),
             has_shield=True)
    ],
    fields=[
        Field(connections=('SW'),
              touching_city=True),
        Field(connections=('SE'),
              touching_city=True)
    ])

tile_T = Tile(
    tile_id='T',
    roads=[
        Road(connections=('S', '-'))
    ],
    cities=[
        City(connections=('N', 'W', 'E'))
    ],
    fields=[
        Field(connections=('SW'),
              touching_city=True),
        Field(connections=('SE'),
              touching_city=True)
    ])

tile_U = Tile(
    tile_id='U',
    roads=[
        Road(connections=('N', 'S'))
    ],
    fields=[
        Field(connections=('NE', 'EN', 'EW', 'WE')),
        Field(connections=('NW', 'WN', 'WS', 'SW'))
    ])

tile_V = Tile(
    tile_id='V',
    roads=[
        Road(connections=('S', 'W'))
    ],
    fields=[
        Field(connections=('SW', 'WS')),
        Field(connections=('NE', 'NW', 'WN', 'EN', 'ES', 'SE'))
    ])

tile_W = Tile(
    tile_id='W',
    roads=[
        Road(connections=('S', '-')),
        Road(connections=('E', '-')),
        Road(connections=('W', '-'))
    ],
    fields=[
        Field(connections=('NW', 'NE', 'EN', 'WN')),
        Field(connections=('SW', 'WS')),
        Field(connections=('ES', 'SE'))
    ])

tile_X = Tile(
    tile_id='X',
    roads=[
        Road(connections=('N', '-')),
        Road(connections=('S', '-')),
        Road(connections=('E', '-')),
        Road(connections=('W', '-'))
    ],
    fields=[
        Field(connections=('NW', 'WN')),
        Field(connections=('SW', 'WS')),
        Field(connections=('NE', 'EN')),
        Field(connections=('SE', 'ES'))
    ])

base_set_tile_quantities = {
    'A': 2,
    'B': 4,
    'C': 1,
    'D': 4,
    'E': 5,
    'F': 2,
    'G': 1,
    'H': 3,
    'I': 2,
    'J': 3,
    'K': 3,
    'L': 3,
    'M': 2,
    'N': 3,
    'O': 2,
    'P': 3,
    'Q': 1,
    'R': 3,
    'S': 2,
    'T': 1,
    'U': 8,
    'V': 9,
    'W': 4,
    'X': 1,
}

tiles = [tile_A, tile_B, tile_C, tile_D, tile_E,
         tile_F, tile_G, tile_H, tile_I, tile_J,
         tile_K, tile_L, tile_M, tile_N, tile_O,
         tile_P, tile_Q, tile_R, tile_S, tile_T,
         tile_U, tile_V, tile_W, tile_X]

BASE_SET = []

for tile in tiles:
    for i in range(base_set_tile_quantities.get(tile.tile_id)):
        BASE_SET.append(tile)

BASE_START_TILE = Tile(
    tile_id='D',
    cities=[
        City(connections=('E'))
    ],
    roads=[
        Road(connections=('N', 'S'))
    ],
    fields=[
        Field(connections=('NE', 'SE'),
              touching_city=True),
        Field(connections=('NW', 'WN', 'WS', 'SW'))
    ])
