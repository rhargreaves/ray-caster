import player as p
import room

class Game():

    def __init__(self):
        self.room = room.Room()
        self.player = p.Player(self.room.centre())

    def move_forward(self):
        self.player.move_forward()
        if self.room.out_of_bounds(self.player.position):
            self.player.move_back()

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

