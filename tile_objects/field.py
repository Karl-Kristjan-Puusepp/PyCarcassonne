
class Field:

    def __init__(self, connections, has_meeple=False):
        self.connections = connections
        self.has_meeple = has_meeple

    @staticmethod
    def __assert_connections_valid(connections):
        for side in connections:
            if side not in ['NE', 'EN', 'ES', 'SE', 'SW', 'WS', 'WN', 'NW', '-']:
                raise TypeError("Road connection tuple received incorrect values")