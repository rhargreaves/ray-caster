#!/usr/bin/env python
import pygame
from game import *

pygame.init()
pygame.display.set_caption("ray-caster")

BLACK = (0, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(1, 10)

game = Game()
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.move_forward()
            if event.key == pygame.K_DOWN:
                game.move_back()
            if event.key == pygame.K_LEFT:
                game.turn_left()
            if event.key == pygame.K_RIGHT:
                game.turn_right()

    game.tick()
    screen.fill(BLACK)
    game.draw(screen)
    pygame.display.flip()
    clock.tick(60)
