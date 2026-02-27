import sys, os
import pygame

from chars.sara import Hero
from chars.reward import Reward
from map.map_loader import load_map

class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        # Scale window to fit 20x20 map with 32x32 tiles
        self.tile_size = 32
        self.map_width = 20
        self.map_height = 20
        self.screen_width = self.tile_size * self.map_width
        self.screen_height = self.tile_size * self.map_height
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = 'Sara Adventure'
        pygame.display.set_caption(self.caption)
        
        # Load map layers
        map_json_path = os.path.join('map', 'sample_map.json')
        try:
            self.layers = load_map(map_json_path)
        except Exception as e:
            print(f"Error loading map: {e}")
            self.layers = {}

        # Initialize Hero with correct path
        hero_sprite_path = os.path.join('assets', 'sara', 'sara_spritesheet.png')
        self.hero = Hero('Sara', hero_sprite_path, 32, 32)
        
        # Initialize Reward (Trophy) at bottom-right area
        self.reward = Reward(self.screen_width - 64, self.screen_height - 64, 32, 32)
        self.game_over = False
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.victory_font = pygame.font.SysFont(None, 72, bold=True)

    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
    def draw_text(self, text, position, color=(255, 255, 255), font=None):
        if font is None:
            font = self.font
        surface = font.render(text, True, color)
        # Add a small shadow/background for better visibility on tiles
        shadow = font.render(text, True, (0, 0, 0))
        self.screen.blit(shadow, (position[0]+2, position[1]+2))
        self.screen.blit(surface, position)

    def handle_input(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            self.hero.left()
        if keys[pygame.K_RIGHT]: 
            self.hero.right()
        if keys[pygame.K_UP]: 
            self.hero.up()
        if keys[pygame.K_DOWN]: 
            self.hero.down()

    def start(self):
        while True:
            self.handle_close()
            self.handle_input()
            elapsed_time = self.clock.tick(60)
            
            # 1. Clear screen
            self.screen.fill((0, 0, 0))
            
            # 2. Draw ground layer
            if 'ground' in self.layers:
                self.layers['ground'].draw(self.screen)
                
            # 3. Draw path layer
            if 'path' in self.layers:
                self.layers['path'].draw(self.screen)
            
            # 4. Draw items layer
            if 'items' in self.layers:
                self.layers['items'].draw(self.screen)
            
            # 5. Draw Reward
            if not self.game_over:
                self.reward.draw(self.screen)
                # Check collision
                if self.hero.rect.colliderect(self.reward.rect):
                    self.game_over = True
            
            # 6. Update and Draw Hero
            self.hero.update(elapsed_time)
            self.hero.draw(self.screen)
            
            # HUD/Text
            self.draw_text("Sara Adventure - Goal: Collect the Trophy!", (10, 10))
            
            # Victory Message
            if self.game_over:
                # Semi-transparent overlay
                overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 150))
                self.screen.blit(overlay, (0,0))
                
                v_text = "VICTORY!"
                v_size = self.victory_font.size(v_text)
                self.draw_text(v_text, (self.screen_width//2 - v_size[0]//2, self.screen_height//2 - 50), (255, 215, 0), self.victory_font)
                
                s_text = "Press ESC to Exit"
                s_size = self.font.size(s_text)
                self.draw_text(s_text, (self.screen_width//2 - s_size[0]//2, self.screen_height//2 + 20))
            
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = SaraAdventure()
    game.start()
