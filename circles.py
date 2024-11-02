import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))

playing=True

black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)

class Circles:
    def __init__(self,size,color,x,y,width):
        self.c=color
        self.s=size
        self.sc=screen
        self.x=x
        self.y=y
        self.w=width
    def draw(self):
        pygame.draw.circle(self.sc,self.c,(self.x,self.y),self.s,self.w)

circle1=Circles(50,red,100,100,0)
circle2=Circles(100,blue,300,300,10)
circle3=Circles(50,green,500,500,0)

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    screen.fill(black)
    circle1.draw()
    circle2.draw()
    circle3.draw()
    pygame.display.update()