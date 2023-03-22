import pygame
from dino_runner.utils.constants import FONT_STYLE, SCORE_SOUND, BUTTON_SOUND, GAME_OVER

class Messages:
    def __init__(self):
        pygame.mixer.init()
        self.font = pygame.font.Font(FONT_STYLE, 32) 
        self.text = ""  
        self.point = 0

#O que será exibido na tela:
    def score(self, screen):
        if self.point == 300 or self.point == 600 or self.point == 1200 or self.point == 2000 or self.point == 3000:
            SCORE_SOUND.play() 

        self.point += 1             
        self.text = self.font.render("Score: " + str(self.point), True, ((0, 0, 0)))
        screen.blit(self.text, (800, 30))

    def game_over(self, screen): 
        screen.blit(GAME_OVER, (350 , 200))

    def level(self, screen):
        if self.point <= 300: 
            self.text = self.font.render("EASY", True, ((0, 0, 0))) 
            screen.blit(self.text, (100, 30))  
        elif self.point <= 600: 
            self.text = self.font.render("MEDIUM", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif self.point <= 1200: 
            self.text = self.font.render("HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))    
        elif self.point <= 2000: 
            self.text = self.font.render("VERY HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif self.point <= 3000 : 
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
            game.screen.blit(GAME_OVER, (350 , 40))
            self.text = self.font.render("Score: " + str(self.point), True, ((0, 0, 0))) 
            game.screen.blit(self.text, (100, 60))
   
            self.text = self.font.render("Death: " + str(game.death_count), True, ((0, 0, 0))) 
            game.screen.blit(self.text, (100, 100))

            t = self.font.render("Press (c) to keep playing", True, (0,0,0))
            t_rect = t.get_rect()
            t_rect.center = (550, 200)
            game.screen.blit(t, t_rect)

            text = self.font.render("Press (f) to start over", True, (0,0,0))
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
                    BUTTON_SOUND.play()
                    game.run()
                elif pygame.key.get_pressed()[pygame.K_c]: #Continuar
                    BUTTON_SOUND.play()
                    game.run()   
                elif pygame.key.get_pressed()[pygame.K_f]: #Botão responsável por recomeçar o jogo do zero. 
                    self.point = 0
                    game.game_speed = 20
                    BUTTON_SOUND.play()
                    game.run()  
                        