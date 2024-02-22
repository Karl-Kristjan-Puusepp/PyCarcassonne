
class Road:

    def __init__(self, connections: tuple, meeple=None):
        self.__assert_connections_valid(connections)
        self.connections = connections
        self.meeple = meeple

    def place_meeple(self):
        pass

    @staticmethod
    def __assert_connections_valid(connections):

        if len(connections) != 2:
            raise TypeError("Road connections tuple has too many values")

        for side in connections:
            if side not in ['N', 'S', 'E', 'W', '-']:
                raise TypeError("Road connection tuple received incorrect values")
