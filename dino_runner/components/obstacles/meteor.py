import random
from dino_runner.components.obstacles.obstacle import Obstacle 
class Meteor(Obstacle):
    def __init__(self, images): #images[0,1]
        self.type =0   #Primeira magem na lista
        self.time = 0  #Intervalos para a animação
        super().__init__(images, self.type)
        self.RANDOM_POS = [198, 280]   #Posições aleatorias para o Meteor
        self.rect.y = random.choice(self.RANDOM_POS)

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        self.time += 1     
        if self.time > 8:  #Controlar o temporizador para animação.
            self.type += 1
            self.time = 0
        if self.type == 2:
            self.type = 0  
#Basicamente a lógica deste modulo é a mesma do Bird.