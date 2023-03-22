import pygame
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
pygame.mixer.init()

#New Aseets:
GAME_OVER = pygame.image.load(os.path.join("dino_runner/assets/other/GameOver.png"))

GAME_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/game_sound.ogg')
GAME_SOUND.set_volume(0.05)

MENU_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/menu_sound.mp3')
MENU_SOUND.set_volume(0.05)

JUMP_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/jump_sound.wav')
JUMP_SOUND.set_volume(0.7)

SCORE_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/score_sound.wav')

BUTTON_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/button_sound.wav')
BUTTON_SOUND.set_volume(0.7)

DEATH_SOUND = pygame.mixer.Sound('dino_runner/assets/Sound/death_sound.ogg')
DEATH_SOUND.set_volume(0.2)

BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, "Background/Background.png"))

BIRD2 = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird6.png"))
]
METEOR = [
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Meteor/8.png")),
] 
# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))


DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Background/Floor.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

SHIELD_TYPE = "shield"
DEFAULT_TYPE = "default"
HAMMER_TYPE = "Hammer"