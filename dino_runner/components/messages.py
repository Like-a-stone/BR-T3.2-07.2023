import pygame
from dino_runner.utils.constants import FONT_STYLE

class Messages:
    def __init__(self):
        pygame.mixer.init()
        self.font = pygame.font.Font(FONT_STYLE, 32) #Fonte que será usada por todos os metodos. 
        self.text = ""  #Atributo para receber os pontos em string, a fonte, e cor.
        self.point = 0

#O que será exibido na tela:
    def score(self, screen):
        if self.point == 300 or self.point == 600 or self.point == 1200 or self.point == 2000 or self.point == 3000:
            self.score_sound = pygame.mixer.Sound('dino_runner/assets/Sound/score_sound.wav') #Efeito de som 
            self.score_sound.play() #Executar o som
        self.point += 1  #Adicionando Pontos
        self.text = self.font.render("Pontuação: " + str(self.point), True, ((0, 0, 0)))
        screen.blit(self.text, (800, 30))

    def game_over(self, screen): # imprimir Game Over na tela 
        self.text = self.font.render("GAME OVER !!!", True, ((0, 0, 0)))
        screen.blit(self.text, (450 , 200))

    def level(self, screen, game_speed):
        if self.point == 300: 
            self.text = self.font.render("EASY", True, ((0, 0, 0))) # Dependendo do score que estamos o texto muda.
            screen.blit(self.text, (100, 30))  
        elif self.point == 600: 
            self.text = self.font.render("MEDIUM", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif self.point == 1200: 
            self.text = self.font.render("HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))    
        elif self.point == 2000: 
            self.text = self.font.render("VERY HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))
        elif self.point == 3000 : 
            self.text = self.font.render("DOOM", True, ((0, 0, 0)))
            screen.blit(self.text, (100, 30))           
    
    def show_menu(self, game): #Irá desenhar o menu principal e menu pos-morte.
        game.screen.fill((255, 255, 255))

        if game.death_count == 0:
            text = self.font.render("Press (s) to start playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (550, 300)
            game.screen.blit(text, text_rect)
        else:
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
        self.button_sound = pygame.mixer.Sound('dino_runner/assets/Sound/button_sound.wav') #efeito de som para botões
        self.button_sound.set_volume(0.7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and game.death_count == 0:
                    self.button_sound.play()
                    game.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.button_sound.play()
                    game.run()   
                elif pygame.key.get_pressed()[pygame.K_f]: #Botão responsável por recomeçar o jogo do zero. 
                    self.point = 0
                    self.button_sound.play()
                    game.run()        