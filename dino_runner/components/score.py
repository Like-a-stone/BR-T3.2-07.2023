import pygame
class Score:
    def __init__(self):
        
        self.font = pygame.font.SysFont("Arial", 32)
        self.point = 0
        self.x = 800
        self.y = 100
        self.text = "tes"
    
    def draw(self, screen):  
        self.point += 1 
        self.text = self.font.render("Pontuação: " + str(self.point), True, ((0, 0, 0))) 
        screen.blit(self.text, (self.x, self.y))

    