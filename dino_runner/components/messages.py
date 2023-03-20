import pygame
class Score:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 32) #Criando atributo para guardar fonte.
        self.point = 0  
        self.x = 800 
        self.y = 30
        self.text = ""  #Atributo para receber os pontos em string, a fonte, e cor.

#Oque será exibido na tela:
    def draw(self, screen):  
        self.point += 1  #Adicionando Pontos
        self.text = self.font.render("Pontuação: " + str(self.point), True, ((0, 0, 0)))#True: deve ser suaviazado?
        screen.blit(self.text, (self.x, self.y))

class GameOver:
    def __init__(self):    #Informações sobre tamanho e fonte de texto
        self.x = 550       #Tamanhos da objeto
        self.y = 300
        self.font = pygame.font.SysFont("Arial", 50)
        self.text = ""

    def draw(self, screen):
        self.text = self.font.render("GAME OVER !!!", True, ((0, 0, 0)))
        pygame.time.wait(500)
        screen.blit(self.text, (self.x, self.y))

class Mode():
    def __init__(self):    #Informações sobre tamanho e fonte de texto
        self.x = 100       #Tamanhos da objeto
        self.y = 30
        self.font = pygame.font.SysFont("Arial", 35)
        self.text = ""

    def draw(self, screen, game_speed):
        if game_speed <= 25: 
            self.text = self.font.render("EASY", True, ((0, 0, 0)))
            screen.blit(self.text, (self.x, self.y))  
        elif game_speed == 30: 
            self.text = self.font.render("MEDIUM", True, ((0, 0, 0)))
            screen.blit(self.text, (self.x, self.y))
        elif game_speed == 35: 
            self.text = self.font.render("HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (self.x, self.y))    
        elif game_speed == 45: 
            self.text = self.font.render("VERY HARD", True, ((0, 0, 0)))
            screen.blit(self.text, (self.x, self.y))
        elif game_speed == 55: 
            self.text = self.font.render("DOOM", True, ((0, 0, 0)))
            screen.blit(self.text, (self.x, self.y))           
