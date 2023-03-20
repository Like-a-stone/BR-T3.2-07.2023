
import random
from dino_runner.components.obstacles.obstacle import Obstacle 

class Bird(Obstacle):
    def __init__(self, images): #images[0,1]
        self.type =0
        self.time = 0
        super().__init__(images, self.type)
        RANDOM_POS = [200, 250, 300]
        self.rect.y = random.choice(RANDOM_POS)

    def draw(self, screen):
        
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        self.time += 1 
        if self.time > 12: #Aqui controlo quanto tempo leva para Bird bate asas.
            self.type += 1
            self.time = 0
        if self.type == 2:
            self.type = 0    
  
          


        