import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.messages import *

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.game_over = GameOver()
        self.Mode = Mode()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.More_Speed() #Nova Função para aumentar dificuldade.
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def More_Speed(self): #Nova Função para aumentar velocidade do jogo conforme o score aumenta.
#Quanto maior for sua pontuação mais rápido o jogo será.
        if self.score.point == 300: 
            self.game_speed += 5      #Easy
        elif self.score.point == 600: 
            self.game_speed += 5      #Medium
        elif self.score.point == 1200:
            self.game_speed += 5      #Hard
        elif self.score.point == 2000:
            self.game_speed += 10     #Very Hard
        elif self.score.point == 4000:
            self.game_speed += 10     #DOOM

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)  

        self.obstacle_manager.update(self)     
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.Mode.draw(self.screen, self.game_speed)


        if not self.playing:
            self.game_over.draw(self.screen)
 
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
