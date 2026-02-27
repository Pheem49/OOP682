import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
ruuning = True
clock = pygame.time.Clock()
while ruuning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
    clock.tick(90)
    pygame.time.delay(100)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f"{clock.get_fps():.2f} FPS", True, (0, 0, 0))
    screen.blit(text, (100, 130))
    pygame.display.update()

pygame.quit()
    