class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0
        self.miss_turn = False

    def can_play(self):
        if self.miss_turn:
            self.miss_turn = False
            return False
        return True

    def opponent(self, players):
        for player in players:
            if player != self:
                return player
