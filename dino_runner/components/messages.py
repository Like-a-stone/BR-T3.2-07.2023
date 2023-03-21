import pygame
from dino_runner.utils.constants import FONT_STYLE
class Messages:
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 32) #Fonte que será usada por todos os metodos. 
        self.text = ""  #Atributo para receber os pontos em string, a fonte, e cor.
        self.point = 0

#O que será exibido na tela:
    def score(self, screen):  

        self.point += 1  #Adicionando Pontos
        self.text = self.font.render("Pontuação: " + str(self.point), True, ((0, 0, 0)))
        screen.blit(self.text, (800, 30))

    def game_over(self, screen):
        self.text = self.font.render("GAME OVER !!!", True, ((0, 0, 0)))
        screen.blit(self.text, (450 , 200))

    def level(self, screen, game_speed):
        if game_speed == 25: 
            self.text = self.font.render("EASY", True, ((0, 0, 0))) # Dependndo do speed que estamos o texto muda.
            screen.blit(self.text, (100, 30))  
        elif game_speed == 30: 
            self.text = self.font.render("MEDIUM", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif game_speed == 35: 
            self.text = self.font.render("HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))    
        elif game_speed == 45: 
            self.text = self.font.render("VERY HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif game_speed == 55: 
            self.text = self.font.render("DOOM", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))           
    
    def show_menu(self, game):
        game.screen.fill((255, 255, 255))
        if game.death_count == 0:
            text = self.font.render("Press (s) to start playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (550, 300)
            game.screen.blit(text, text_rect)
        else:
            text = self.font.render("Press (c) to start playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (550, 300)
            game.screen.blit(text, text_rect)

        pygame.display.update() 

        self.handle_events_on_menu(game)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and game.death_count == 0:
                    game.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    game.run()     