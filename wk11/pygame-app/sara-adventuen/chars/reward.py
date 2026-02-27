import pygame
from pygame.sprite import Sprite
import os

class Reward(Sprite):
    def __init__(self, x, y, width=32, height=32):
        super().__init__()
        # Load the trophy image
        trophy_path = os.path.join('assets', 'items', 'gold_trophy.png')
        self.image = pygame.image.load(trophy_path).convert_alpha()
        # Scale to match tile size
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
