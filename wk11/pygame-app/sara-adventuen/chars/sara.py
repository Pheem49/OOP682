import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    def __init__(self, name, filename, x, y, rows=4, cols=3, width=32, height=32):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet.set_colorkey((255, 255, 255))
        
        # Spritesheet is 640x640 with 3 cols and 4 rows
        # Each frame is 640/3 x 640/4 (approx 213x160)
        self.sheet_width, self.sheet_height = self.sheet.get_size()
        self.frame_w = self.sheet_width // cols
        self.frame_h = self.sheet_height // rows
        
        self.row = 0
        self.col = 0
        self.elapsed_time = 0
        self.rect = pygame.Rect(x, y, width, height)
        # Store requested size for scaling
        self.display_width = width
        self.display_height = height

    def update(self, elapsed_time):
        self.elapsed_time += elapsed_time
        if self.elapsed_time > 150: # Slightly slower animation
            self.col = (self.col + 1) % 3
            self.elapsed_time -= 150

    def left(self): 
        self.rect.x -= 5
        self.row = 2 # Left facing row (looking at the sheet)
    def right(self): 
        self.rect.x += 5
        self.row = 3 # Right facing row
    def up(self): 
        self.rect.y -= 5
        self.row = 1 # Back facing row
    def down(self): 
        self.rect.y += 5
        self.row = 0 # Front facing row

    def draw(self, surface):
        # Get the source frame
        src_rect = pygame.Rect(self.col * self.frame_w, self.row * self.frame_h, self.frame_w, self.frame_h)
        frame = self.sheet.subsurface(src_rect)
        # Scale it to fit the game size
        scaled_frame = pygame.transform.scale(frame, (self.display_width, self.display_height))
        surface.blit(scaled_frame, self.rect)