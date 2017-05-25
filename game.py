import pygame
import math

WHITE = (255, 255, 255)
SPEED = 5
PI = 3.141592
ARROW_LENGTH = 50

class Game():

    def __init__(self):
        self.position = [250, 250]
        self.angle = 0

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

    def turn_left(self):
        self.angle -= 0.25

    def turn_right(self):
        self.angle += 0.25

    def draw(self, screen):
        pygame.draw.line(screen, 
                WHITE, 
                self.position, 
                [self.position[0] + (math.sin(self.angle) * ARROW_LENGTH),
                 self.position[0] + (math.cos(self.angle) * ARROW_LENGTH)],
                1)

