import pygame
import math


class Bullet:
    def __init__(self, x, y, direct_x, direct_y, window):
        self.x, self.y = x, y
        self.starting_x = x
        self.window = window
        self.direct_x = direct_x
        self.direct_y = direct_y
        self.a = (y - direct_y) / (x - direct_x) if x-direct_x != 0 else 10**9
        self.b = self.y - self.a * self.x
        self.alpha = math.atan(self.a)
        self.speed = 10
        self.W, self.H = 15, 15
        self.img = pygame.image.load('W..png')
        self.img = pygame.transform.scale(self.img, (self.W, self.H))
        self.remove = False

    def move(self):
        if self.direct_x >= self.starting_x:
            self.x += self.speed * math.cos(self.alpha)
            self.y += self.speed * math.sin(self.alpha)
        else:
            self.x -= self.speed * math.cos(self.alpha)
            self.y -= self.speed * math.sin(self.alpha)
