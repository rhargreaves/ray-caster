import pygame

WHITE = (255, 255, 255)
SPEED = 5

class Game():

    def __init__(self):
        self.position = [250, 250]

    def tick(self):
        return

    def move_forward(self):
        self.position = [self.position[0], self.position[1]-SPEED]

    def move_back(self):
        self.position = [self.position[0], self.position[1]+SPEED]

    def move_left(self):
        self.position = [self.position[0]-SPEED, self.position[1]]

    def move_right(self):
        self.position = [self.position[0]+SPEED, self.position[1]]

    def draw(self, screen):
        pygame.draw.line(screen, 
                WHITE, 
                self.position, 
                [v+50 for v in self.position], 
                1)

