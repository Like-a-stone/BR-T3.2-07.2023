import pygame

from dino_runner.utils.constants import *
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
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.pos_Cloud = SCREEN_WIDTH
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.messages= Messages()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.messages.show_menu(self)  
    pygame.display.quit() 
    pygame.quit()        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.More_Speed() #Nova Função para aumentar dificuldade.
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(650)
        

    def More_Speed(self): #Nova Função para aumentar velocidade do jogo conforme o score aumenta.
#Quanto maior for sua pontuação mais rápido o jogo será.
        if self.messages.point == 300: 
            self.game_speed += 3      #Easy
        elif self.messages.point == 600: 
            self.game_speed += 5      #Medium
        elif self.messages.point == 1200:
            self.game_speed +=  8    #Hard
        elif self.messages.point == 2000:
            self.game_speed += 6      #Very Hard
        elif self.messages.point == 3000:
            self.game_speed += 10      #DOOM

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.execute = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)  

        self.obstacle_manager.update(self)     
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud() #Novo desenho para nuvem
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.messages.score(self.screen)
        self.messages.level(self.screen, self.game_speed)

        if not self.playing:
            self.messages.game_over(self.screen)
 
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

    def cloud(self):
        self.screen.blit(CLOUD, (self.pos_Cloud, 200)) #Como a nuvem deve ser desenhada na tela.
        self.pos_Cloud -=  self.game_speed -15  # Movimento da nuvem
        if self.pos_Cloud < -SCREEN_WIDTH:    # Se a nuvem alcançar o canto da tela, outra aparecerá
            self.pos_Cloud = SCREEN_WIDTH


       
        
