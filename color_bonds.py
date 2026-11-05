import pygame
import random

pygame.init()


SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT =  pygame.USEREVENT + 2

BLUE = pygame.color('blue')
RED = pygame.color('red')
LIGTHBLUE= pygame.color('ligthblue')


YELLOW = pygame.color ('yellow')
ORANGE = pygame.color ('orange')
RED = pygame.color ('red')
GREEN = pygame.color ('green')

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color , heigh, width):
        super().__init__()

        self.image = pygame.surface([width,heigh])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.veloctiy = [random.choice([-1 , 1 ]) , random.choice([-1 , 1 ])]


    def update(self):
        self.rect.move_iq(self.veloctiy)

        boundary_hit  =  False

        if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocti[0] = -self.veloctiy[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
                    self.velocti[1] = -self.veloctiy[1]
                    boundary_hit = True


        if boundary_hit:
              pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
              pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))


    def change_color(self):
          self.image.fill(random.choice([YELLOW ,ORANGE,RED,GREEN]))


def change_background_color(self):
      global bg_color
      bg_color = random.choice(BLUE,LIGTHBLUE,RED)
      