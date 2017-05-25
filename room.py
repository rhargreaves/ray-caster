import pygame

YELLOW = (255, 255, 0)

class Room():

    def __init__(self):
        self.vertices = [
                (50, 50), (250, 50),
                (250, 250), (50, 250)
            ]

    def draw(self, screen):
        pygame.draw.polygon(screen, YELLOW, self.vertices, 1)
