
class Monastery:

    def __init__(self, has_meeple=False):
        self.has_meeple = has_meeple

    def place_meeple(self):
        self.has_meeple = True