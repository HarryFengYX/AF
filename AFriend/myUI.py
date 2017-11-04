#the UI that pygame runs
import pygame
from pygameUIlib import *
pygame.init()
pygame.font.init()
WHITE = (255,255,255)
BLACK = (0, 0, 0)


        

        
        
mygame = pygameobj('my UI', (1500, 800))
clock = pygame.time.Clock()
crashed = False

mygame.gameDisplay.fill(WHITE)
mytext = single_line_text('Hello, World', 40, BLACK)
para = 'Hello, I am Yinxuan. I am trying out this long sentence feature to see if it works as good as the way that I expect it to be, which I must admit, is difficult and achieveable'
mypara = mutiple_line_text(para, 20, BLACK, 40)
myblock = title_text(mytext, mypara)
myrect = interactive_rectangle()
my_inter_text = interactive_text(myrect, myblock)
while (not crashed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    #mytext.play((0,0), mygame.gameDisplay)
    #mypara.play((0, 100), mygame.gameDisplay)
    #myrect.play((0,0), mygame.gameDisplay)
    #myblock.play((0,0), mygame.gameDisplay)
    mytext.transform(1,(0,0),mygame.gameDisplay)
    my_inter_text.play((100,200), mygame.gameDisplay)
    
    pygame.display.update()
    clock.tick(20)
    mygame.gameDisplay.fill(WHITE)