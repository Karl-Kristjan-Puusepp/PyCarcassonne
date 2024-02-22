
class Field:

    def __init__(self, connections,
                 meeple=None,
                 touching_city=False):
        self.connections = connections
        self.meeple = meeple
        self.touching_city = touching_city

    def place_meeple(self):
        pass
    @staticmethod
    def __assert_connections_valid(connections):
        for side in connections:
            if side not in ['NE', 'EN', 'ES', 'SE', 'SW', 'WS', 'WN', 'NW']:
                raise TypeError("Road connection tuple received incorrect values")