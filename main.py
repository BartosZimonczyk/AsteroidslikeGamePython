import pygame
from player import Player
from block import Block
from bullet import Bullet
import intervals as I
from copy import copy


class Window:
    def __init__(self):
        self.H = 800
        self.W = 1200
        self.GameDisplay = None
        self.background = (200, 150, 180, 255)
        self.clock = pygame.time.Clock()
        self.last_window = None
        self.FPS = 60
        self.font_size = 20
        self.font = None
        self.time = 0
        self.freq = 20
        self.points = 0
        self.player = Player(self)
        self.blocks = list()
        self.bullets = list()

    def draw_object(self, obj):
        self.GameDisplay.blit(obj.img, (obj.x, obj.y))

    def draw_menu(self):
        num_blocks = len([block for block in self.blocks if block.y > 0])
        blocks = self.font.render('Blocks: {}'.format(num_blocks), True, (0, 0, 0))
        rect = blocks.get_rect()
        rect.topleft = (0, 0)
        self.GameDisplay.blit(blocks, rect)
        blocks = self.font.render('New blocks per second: {}'.format(round(self.FPS/self.freq, 2)), True, (0, 0, 0))
        rect = blocks.get_rect()
        rect.topleft = (0, self.font_size)
        self.GameDisplay.blit(blocks, rect)
        blocks = self.font.render('Bullets: {}'.format(len(self.bullets)), True, (0, 0, 0))
        rect = blocks.get_rect()
        rect.topleft = (0, 2*self.font_size)
        self.GameDisplay.blit(blocks, rect)
        blocks = self.font.render('Points: {}'.format(self.points), True, (0, 0, 0))
        rect = blocks.get_rect()
        rect.topleft = (0, 3 * self.font_size)
        self.GameDisplay.blit(blocks, rect)

    def shoot(self, mouse):
        self.bullets.append(Bullet(self.player.x + self.player.size/2, self.player.y, mouse[0], mouse[1], self))

    def play(self):
        pygame.init()
        self.GameDisplay = pygame.display.set_mode((self.W, self.H), 0)
        self.GameDisplay.fill(self.background)
        self.font = pygame.font.Font('TypewriterScribbled.ttf', self.font_size)
        quit_game = False
        while not quit_game:
            self.time += 1
            self.GameDisplay.fill(self.background)
            self.draw_menu()
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.draw_object(self.player)
            if self.time % 7 == 0:
                mouse = pygame.mouse.get_pos()
                self.shoot(mouse)
            if self.time % 180 == 0:
                if self.freq > 1:
                    self.freq -= 1
            if self.time % self.freq == 0:
                self.blocks.append(Block(self))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                    pygame.quit()
                    quit()
            self.blocks = [block for block in self.blocks if block.y <= self.H]
            for block in self.blocks:
                if I.closed(block.x, block.x+block.W).overlaps(I.closed(self.player.x, self.player.x+self.player.size))\
                        and I.closed(block.y, block.y+block.W).overlaps(I.closed(self.player.y, self.player.y+self.player.size)):
                    quit_game = True
                    #pygame.quit()
                    #quit()
                block.move()
                self.draw_object(block)
            self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.x <= self.W and 0 <= bullet.y <= self.H]
            for bullet in self.bullets:
                bullet.move()
                self.draw_object(bullet)
                a = copy(len(self.blocks))
                self.blocks = [block for block in self.blocks
                               if not I.closed(block.x, block.x + block.W).overlaps(I.closed(bullet.x, bullet.x + bullet.W))
                               or not I.closed(block.y, block.y + block.H).overlaps(I.closed(bullet.y, bullet.y + bullet.H))]
                bullet.remove = (a != len(self.blocks))
                if bullet.remove:
                    self.points += 1
            self.bullets = [bullet for bullet in self.bullets if not bullet.remove]
            pygame.display.flip()
            self.clock.tick(self.FPS)

        print(self.points)


if __name__ == '__main__':
    w = Window()
    w.play()
