import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    def __init__(self, name, filename, x, y, rows=2, cols=3, width=34, height=56):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.row = 0
        self.col = 0
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 200 * dt / 1000
        if keys[pygame.K_RIGHT]:
            self.rect.x += 200 * dt / 1000
        if keys[pygame.K_UP]:
            self.rect.y -= 200 * dt / 1000
        if keys[pygame.K_DOWN]:
            self.rect.y += 200 * dt / 1000

    def draw(self, surface):
        frame = self.sheet.subsurface(
                    self.col * self.rect.width, 
                    self.row * self.rect.height, 
                    self.rect.width, self.rect.height)
        surface.blit(frame, self.rect)