import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
ruuning = True
sara = pygame.image.load('sara/sara-cal1.png')
clock = pygame.time.Clock()
while ruuning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ruuning = False
    clock.tick(90)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f"{clock.get_fps():.2f} FPS", True, (0, 0, 0))
    screen.blit(text, (50, 230))
    screen.blit(sara, (50, 50))
    pygame.display.update()
pygame.quit()
    