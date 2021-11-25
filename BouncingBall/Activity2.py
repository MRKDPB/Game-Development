# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:01:09 2021

@author: Bhagyashree

Python Capstone Projects: 
    Activity 2- Bouncing Ball
    
"""
import random
import pygame

pygame.init()

pygame.mixer.music.load('mixkit-game-ball-tap-2073.wav')


color = (0, random.randint(0,25), random.randint(0,255))
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bouncing Ball")
x = 200
y = 200
v = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill((255,255,255))
    pygame.draw.circle(screen, color, (x,y), 20)
    y += v
    if y == 380 or y == 20:
        pygame.mixer.music.play(0)
        v = -v
    
    pygame.display.update() 
    pygame.time.wait(10)
            