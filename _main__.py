"""A game I wanted to make in Python (no docstring originality)"""
import pygame
from pygame import display

pygame.init()
window = display.set_mode((800, 600))
display.set_caption("Islands")

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
