import pygame
pygame.init()
class pygameobj:   
    def __init__(self, title, dimen):
        
        pygame.display.set_caption('MY UI')
        self.gameDisplay = pygame.display.set_mode(dimen)
        self.width, self.height = dimen
        
class single_line_text:
    def __init__(self, text, size=50, color=(0,0,0), font='cambria'):
        pygame.font.init()
        self.myfont = pygame.font.SysFont(font, size)
        self.textobj = self.myfont.render(text, True, color)
        self.size = size
        self.color = color
        self.text = text
        
    def play(self, position, screen):
        screen.blit(self.textobj, position)   
        
    def transform(self, size, position, screen):
        screen.blit(pygame.transform.flip(self.textobj, 1, 1), position)
        
class mutiple_line_text:
    def __init__(self, text, size=20, color=(0,0,0), line_length=40, font='cambria'):
        self.text = text
        self.size = size
        self.color = color
        self.line_length = line_length
        self.font = font
        self.myfont = pygame.font.SysFont(font, size)
        self.find_format()
        
    def find_format(self):
        textlist = self.text.split(' ')
        eachline = []
        thisline = ''
        for i in textlist:
            if i is textlist[-1]:
                eachline.append(' '+i)
            elif (len(thisline)+len(i)) <= self.line_length:
                thisline += ' '+i
            else:
                eachline.append(thisline)
                thisline = ''
        self.eachline = eachline
        
    def play(self, position, screen):
        for i in range(len(self.eachline)):
            textobj = self.myfont.render(self.eachline[i], True, self.color)
            #print(self.eachline[i])
            x, y = position
            y += i*self.size
            real_position = (x, y)
            screen.blit(textobj, real_position)
            
class interactive_rectangle:
    def __init__(self, size=(400, 400), color=(200,200,200)):
        self.size = size
        self.color = color
           
    def play(self, position, screen):
        myrect = pygame.Rect(position + self.size)
        pygame.draw.rect(screen, self.color, myrect)
        
            
class title_text:
    def __init__(self, single_line_obj, multi_line_obj):
        self.title = single_line_obj
        self.para = multi_line_obj
        
    def play(self, position, screen):
        self.title.play(position, screen)
        x, y = position
        para_position = (x, y+50)
        self.para.play(para_position, screen)
        
class interactive_text:
    def __init__(self, inter_rect, textobj):
        self.rect = inter_rect
        self.text = textobj
    
    def play(self, position, screen):
        self.rect.play(position, screen)
        x,y = position
        realposition = (x+20, y+40)
        self.text.play(realposition, screen)
        
class video:
    def __init__(self, fn):
        self.fn = fn
        self.cap = cv2.VideoCapture(fn)
        
    def play(self, position, size, gameDisplay):
        self.capcheck()
        self.ret, self.frame = self.cap.read()
        self.rows,self.cols,self.ch = self.frame.shape
        self.FX = size[0]/self.cols
        self.FY = size[1]/self.rows     
        self.carImg = cv2.resize(self.frame,None,fx=self.FX, fy=self.FY, interpolation = cv2.INTER_CUBIC)
        self.carImg = np.rot90(np.fliplr(self.carImg))
        self.carImg = pygame.surfarray.make_surface(self.carImg)
        gameDisplay.blit(self.carImg, position)
        
        
    def capcheck(self):
        if not self.cap.isOpened():
            self.cap = cv2.VideoCapture(self.fn)
            
class schedule:
    pass
