
class Road:

    def __init__(self, connections: tuple):
        self.__assert_connections_valid(connections)
        self.connections = connections

    def set_connections(self, connections: tuple):
        self.__assert_connections_valid(connections)
        self.connections = connections

    @staticmethod
    def __assert_connections_valid(connections):

        if len(connections) != 2:
            raise TypeError("Road connections tuple has too many values")

        for side in connections:
            if side not in ['N', 'S', 'E', 'W', '-']:
                raise TypeError("Road connection tuple received incorrect values")
