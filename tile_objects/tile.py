from tile_objects.road import Road
from tile_objects.city import City
from tile_objects.field import Field
from tile_objects.monastery import Monastery

class Tile:
    def __init__(self,
                 tile_id=None,
                 roads=None,
                 cities=None,
                 fields=None,
                 monastery=None,
                 has_meeple=False,
                 meepled_feature=None):
        self.tile_id = tile_id
        self.roads = roads
        self.cities = cities
        self.fields = fields
        self.monastery = monastery
        self.has_meeple = has_meeple
        self.meepled_feature = meepled_feature

    def rotate(self, times):
        pass

    def get_side_feature(self, side):  # N, S, E, W
        pass                           # "Field", "Road", "City"

    def place_meeple(self, feature):
        if self.has_meeple:
            raise ValueError("Cannot place meeple on already occupied tile.")
        pass # TODO


    def remove_meeple(self):
        self.has_meeple = False # TODO - remove meeple from feature
