import player

class Game():

    def __init__(self):
        self.player = player.Player()

    def move_forward(self):
        self.player.move_forward()

    def move_back(self):
        self.player.move_back()

    def turn_left(self):
        self.player.turn_left()

    def turn_right(self):
        self.player.turn_right()

    def tick(self):
        return

    def draw(self, screen):
        self.player.draw(screen)

