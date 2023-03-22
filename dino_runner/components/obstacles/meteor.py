import random
from dino_runner.components.obstacles.obstacle import Obstacle 
class Meteor(Obstacle):
    def __init__(self, images): 
        self.type =0  
        self.time = 0  
        super().__init__(images, self.type)
        self.rect.y = 0
        self.rect.x = 1000

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
        self.time += 1     
        if self.time > 2:  
            self.type += 1
            self.time = 0
        if self.rect.y < 300:
            if self.type == 5:
               self.type = 0 
        else:
            if self.type == 8:
                self.type = 6

    def update(self, game_speed, obstacles):
        self.rect.y += 10
        self.rect.x -= 25

        if self.rect.x < -self.rect.width:
            obstacles.pop()  
        if self.rect.y > 390:
            obstacles.pop() 
