import pygame, cv2
import numpy as np

pygame.init()

display_width = 950
display_height = 500

class pygameobj:
    def __init__(self, title, dimen):
        pygame.display.set_caption('MY UI')
        self.gameDisplay = pygame.display.set_mode(dimen)

mygame = pygameobj('my UI', (1920, 1080))
clock = pygame.time.Clock()
crashed = False
cap = cv2.VideoCapture('Landscapes - Volume 4K (UHD)-9ZfN87gSjvI.mp4')

class video:
    def __init__(self, fn):
        self.cap = cv2.VideoCapture(fn)
        
        
    def play(self, position, size, gameDisplay):
        self.ret, self.frame = self.cap.read()
        self.rows,self.cols,self.ch = self.frame.shape
        self.FX = size[0]/self.cols
        self.FY = size[1]/self.rows     
        self.carImg = cv2.resize(self.frame,None,fx=self.FX, fy=self.FY, interpolation = cv2.INTER_CUBIC)
        self.carImg = np.rot90(np.fliplr(self.carImg))
        self.carImg = pygame.surfarray.make_surface(self.carImg)
        gameDisplay.blit(self.carImg, position)
mygame.gameDisplay.fill((0,0,0))
mv = video('Landscapes - Volume 4K (UHD)-9ZfN87gSjvI.mp4')
while (not crashed) and cap.isOpened():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True    
    #ret, frame = cap.read()
    #rows,cols,ch = frame.shape
    #FX = display_width/cols/n
    #FY = display_height/rows/n
    #res = cv2.resize(frame,None,fx=FX, fy=FY, interpolation = cv2.INTER_CUBIC)    
    #carImg = res
    #carImg = np.rot90(np.fliplr(carImg))
    #carImg = pygame.surfarray.make_surface(carImg)
    

    #mygame.gameDisplay.fill(white)
    mv.play((0,0),(1920, 1080), mygame.gameDisplay)
    
        
    pygame.display.update()
    clock.tick(20)
    mygame.gameDisplay.fill((255,255,255))

pygame.quit()
quit()
cap.release()
