import pygame
import random

SCREEN_WIDTH , SCREEN_HEIGHT = 700,750
MOVEMENT_SPEED = 4
FONT_SIZE = 72

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.webp"),
                                         (SCREEN_WIDTH , SCREEN_HEIGHT))


font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(
            pygame.Color("dodgreblue"))
        pygame.draw.rect(self.image, color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    