import pygame
import math
from copy import copy


class Player:
    def __init__(self, window):
        self.R = 25
        self.window = window
        self.x, self.y = math.floor(self.window.W/2), math.floor(7*self.window.H/8)
        self.color = (200, 50, 50)
        self.move_speed = 4
        self.size = 50
        self.center = (self.x + self.size/2, self.y + self.size/2)
        self.img = pygame.image.load('BK.png')
        self.img = pygame.transform.scale(self.img, (self.size, self.size))

    def move(self, keys):
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < self.window.H - self.size:
            self.y += self.move_speed
            self.center = (self.x + self.size / 2, self.y + self.size / 2)
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 0:
            self.y -= self.move_speed
            self.center = (self.x + self.size / 2, self.y + self.size / 2)
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.move_speed
            self.center = (self.x + self.size / 2, self.y + self.size / 2)
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < self.window.W - self.size:
            self.x += self.move_speed
            self.center = (self.x + self.size / 2, self.y + self.size / 2)

