import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.messages import Messages
from dino_runner.utils.constants import DEFAULT_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.messages =Messages()
    
    def generate_power_up(self):
        if len(self.power_ups) == 0 or self.when_appears == self.messages.point:
            self.when_appears += random.randint(500,600)
           
            random_power_ups = random.randint(0, 1) 
            if random_power_ups== 0:            
                self.power_ups.append(Shield())
               
            elif random_power_ups == 1:
                self.power_ups.append(Hammer())
               
            
    def update(self, game):
        self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield = True
                    player.has_power_up = True
                    player.type = power_up.type#tipo de image que estaria utilizando
                    player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)

    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(200,300)# es necessario esto?