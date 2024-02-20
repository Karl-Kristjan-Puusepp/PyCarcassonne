from game_objects.tilesets import BASE_SET
import random


class Tilebag:
    def __init__(self, tileset=BASE_SET):
        self.tileset = tileset

    def shuffle(self):
        random.shuffle(self.tileset)

    def draw_tile(self):
        return self.tileset.pop()

    def __len__(self):
        return len(self.tileset)

    def is_empty(self):
        return True if len(self.tileset) == 0 else False
