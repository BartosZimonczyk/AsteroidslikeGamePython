import pygame
import math
import random


class Block:
    def __init__(self, window):
        self.window = window
        self.W = random.randint(10, 60)
        self.H = random.randint(self.W, 60)
        self.x = random.randint(0, self.window.W-self.W)
        self.y = -100
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = 1
        self.img = pygame.Surface((self.W, self.H))
        self.img.set_alpha(200)
        self.img.fill(self.color)
        self.acceleration = self.W*self.H/5/60**2

    def move(self):
        self.y += self.speed
        self.speed += self.acceleration

