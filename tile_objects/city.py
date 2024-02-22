
class City:

    def __init__(self, connections,
                 has_shield=False,
                 meeple=None):
        self.__assert_connections_valid(connections)
        self.connections = connections
        self.has_shield = has_shield
        self.meeple = meeple

    def place_meeple(self):
        pass

    @staticmethod
    def __assert_connections_valid(connections):

        if len(connections) > 4 or len(connections) < 0:
            raise TypeError("City connections tuple has too many values")

        for side in connections:
            if side not in ['N', 'S', 'E', 'W', '-']:
                raise TypeError("Road connection tuple received incorrect values")