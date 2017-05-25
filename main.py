#!/usr/bin/env python
import pygame

pygame.init()
pygame.display.set_caption("ray-caster")

WHITE = (0, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.display.flip()
    clock.tick(60)
