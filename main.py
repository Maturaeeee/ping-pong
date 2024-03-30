from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10 
RESTART_TIME = 3000

def get_color():
    return (randint(0,255),randint(0,255),randint(0,255))

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

backgroung = get_color()
window = display.set_mode((WIDTH, HEIGHT))
window.fill(backgroung)
display.set_caption("Ping-pong")
clock = time.Clock()

run = True
color_selection = Falsefinish = False
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                color_selection = True
        elif e.type == KEYUP:
            if e.key == K_SPACE:
                color_selection = False
    
    if not finish: 
        if color_selection:
            backgroung = get_color()
        window.fill(backgroung)  
    else:
        pass 
    
    display.update()
    clock.tick(FPS)
