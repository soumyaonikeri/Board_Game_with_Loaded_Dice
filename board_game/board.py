class Board:
    def __init__(self, layout):
        self.layout = layout
        self.size = len(layout)

    def move_player(self, player, steps, players):
        player.position = (player.position + steps) % self.size
        current_square = self.layout[player.position]
        if current_square == 'B':
            self.land_on_bank(player)
        elif current_square == 'J':
            self.land_on_jail(player)
        elif current_square == 'H':
            self.land_on_house(player, players)

    def land_on_bank(self, player):
        player.balance += 10
        # Prompt user for optional actions (taking a loan, repaying debt) will be handled in CLI

    def land_on_jail(self, player):
        player.balance -= 20
        player.miss_turn = True

    def land_on_house(self, player, players):
        if player.balance > 0:
            player.balance += 2
        else:
            player.balance -= 2

        if player.debt > 0:
            player.debt += 1

        # Handle the case where another player is on the same square
        for p in players:
            if p != player and p.position == player.position:
                if player.balance > 0:
                    p.balance += round(player.balance * 0.5)
