from __future__ import division
import pygame

YELLOW = (255, 255, 0)

class Room():

    def __init__(self):
        self.vertices = [
                (75, 75), (350, 75),
                (350, 350), (75, 350)
            ]

    def centre(self):
        return (sum([x for x,_ in self.vertices]) / len(self.vertices),
                sum([y for _,y in self.vertices]) / len(self.vertices))

    def draw(self, screen):
        pygame.draw.polygon(screen, YELLOW, self.vertices, 1)
