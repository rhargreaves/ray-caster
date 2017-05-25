from __future__ import division
import pygame
import math

WHITE = (255, 255, 255)
SPEED = 5
ARROW_LENGTH = 25
ANGLE_STEP = SPEED / 40

class Player():

    def __init__(self, position):
        self.position = position
        self.angle = 0

    def move_forward(self):
        self.position = [
                self.position[0] - (math.sin(self.angle) * SPEED),
                self.position[1] + (math.cos(self.angle) * (SPEED * -1))]

    def move_back(self):
        self.position = [
                self.position[0] + (math.sin(self.angle) * SPEED),
                self.position[1] - (math.cos(self.angle) * (SPEED * -1))]

    def turn_left(self):
        self.angle += ANGLE_STEP

    def turn_right(self):
        self.angle -= ANGLE_STEP

    def draw(self, screen):
        pygame.draw.line(screen, 
                WHITE, 
                self.position, 
                [self.position[0] - (math.sin(self.angle) * ARROW_LENGTH),
                 self.position[1] - (math.cos(self.angle) * ARROW_LENGTH)],
                1)

