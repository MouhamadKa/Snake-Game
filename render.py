import config
import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen
        self.green = config.COLORS['green']
        self.red = config.COLORS['red']
        self.white = config.COLORS['white']
        self.background = config.COLORS['navy']
        self.block_size = config.BLOCK_SIZE
        self.font = pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        
    def draw_background(self):
        self.screen.fill(self.background)
        
    def draw_snake(self, snake):
        for x, y in snake.snake_body:
            pygame.draw.rect(self.screen, self.green, [x, y, self.block_size, self.block_size])
            
    def draw_food(self, food):
        x, y = food.position
        pygame.draw.rect(self.screen, self.red, [x, y, self.block_size, self.block_size])
        
    def draw_score(self, score):
        text = self.font.render(f'Score: {score}', True, self.white)
        self.screen.blit(text, config.SCORE_POSITION)
        
    def draw_game_over(self):
        text = self.font.render(f'Game Over', True, self.white)
        center_x = self.screen.get_width() // 2 - text.get_width() // 2
        center_y = self.screen.get_height() // 2 - text.get_height() // 2
        self.screen.blit(text, (center_x, center_y))
        