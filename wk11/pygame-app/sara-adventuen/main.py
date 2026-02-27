import sys, os
import pygame
from char.sara import Hero

class SavaAdventurer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.caption = 'Sava Adventurer'
        self.hero = Hero('Sara', 'sara/sara-cal1.png', 50,50)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        pygame.display.set_caption(self.caption)

    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_text(self, text, position, color=(0, 0, 0)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=position)
        self.screen.blit(surface, rect)
    
    def start(self):
        while True:
            self.handle_close()
            self.screen.fill((255, 255, 255))
            self.draw_text('Sara Adventurer', (620, 350))
            self.hero.update(self.clock.get_time())
            self.hero.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__':
    game = SavaAdventurer()
    game.start()