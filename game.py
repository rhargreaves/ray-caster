import player
import room

class Game():

    def __init__(self):
        self.player = player.Player()
        self.room = room.Room()

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
        self.room.draw(screen)

