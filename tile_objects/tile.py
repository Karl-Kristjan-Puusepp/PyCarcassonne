from tile_objects.road import Road


class Tile:
    def __init__(self,
                 tile_id=None,
                 roads=None,
                 cities=None,
                 fields=None,
                 monastery=False,
                 has_meeple=False):
        self.tile_id = tile_id
        self.roads = roads
        self.cities = cities
        self.fields = fields
        self.monastery = monastery
        self.has_meeple = has_meeple

    def rotate(self, times):
        pass

    def get_side_feature(self, side):  # N, S, E, W
        pass

    def add_meeple(self, feature):
        pass

    def remove_meeple(self):
        self.has_meeple = False
