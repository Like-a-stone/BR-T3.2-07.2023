import pygame
class GameOver:
    def __init__(self):    #Informações sobre tamanho e fonte de texto
        self.x = 550 
        self.y = 300
        self.font = pygame.font.SysFont("Arial", 50)
        self.text =  " "

    def draw(self, screen):
       #Oque será exibido na tela.
        self.text = self.font.render("GAME OVER !!!", True, ((0, 0, 0)))
        screen.blit(self.text, (self.x, self.y))
        pygame.time.wait(500)
        
        
