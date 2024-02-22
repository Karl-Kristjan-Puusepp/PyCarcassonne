class Player:
    def __init__(self,
                 color,
                 score=0,
                 meeples=7):  # TODO - fix shit
        if color not in ["BLUE, YELLOW, GREEN, RED, BLACK"]:
            raise ValueError(f"Disallowed color for player object: {color}")
        self.color = color
        self.score = score
        self.meeples = meeples
