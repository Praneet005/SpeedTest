import pygame
from pygame.locals import *
import sys
import time
import random

# 750 x 500    
    
class Game:
   
    def _init_(self):
        self.w=750
        self.h=500
        self.reset=True
        self.active = False
        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
       
        pygame.init()
        self.open_img = pygame.image.load(r"C:\Users\gouth\Desktop\COMPUTER SCIENCE PROGRAMS\card.png")
        self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h))


        self.bg = pygame.image.load(r"C:\Users\gouth\Desktop\COMPUTER SCIENCE PROGRAMS\colour.jpg")
        self.bg = pygame.transform.scale(self.bg, (500,750))

        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Word Practice')
       
        
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()   
        
    def get_sentence(self):
        tb=''
        f = open(r"C:\Users\gouth\Desktop\COMPUTER SCIENCE PROGRAMS\top 200 words.txt").read()
        sentences = f.split()
        for i in range(2):
            sentence = random.choice(sentences) + ' '
            tb += sentence + ' '
        return tb

    def show_results(self, screen):
        if(not self.end):

            self.total_time = time.time() - self.time_start
            
            p=self.word             #given string
            p1=self.input_text      #input string
            l = len(p)
            a=p1.split()            #input string split
            b=p.split()             #given string split
            q=0
            for i in range(len(a)):
                q+=len(a[i])
            c=0
            for i in range(len(b)):
                if len(b[i]) > len(a[i]):
                    diff=len(b[i])-len(a[i])
                    for j in range(diff):
                        a[i] += " "
                else:
                    diff=len(a[i])-len(b[i])
                    for j in range(diff):
                        b[i] += " "
            for f in range(len(a)):
                for j in range(len(a[f])):
                    if b[f][j] == a[f][j]:
                        c=c+1
                    else:
                        c=c-1/3.45
            if c<0:
                c=0
            
            self.acc=(c/q)*100
            self.acc=str(self.acc)
            self.acc=self.acc[0:5]
            self.acc=float(self.acc)

           
            self.wpm = len(p1)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)
                
            self.results = 'Time:'+str((str(self.total_time)[0:4])) +" secs   Accuracy:"+ str(round(self.acc)) + "%" + '   Wpm: ' + str(round((self.wpm*self.acc)/100))


            self.time_img = pygame.image.load(r"C:\Users\gouth\Desktop\COMPUTER SCIENCE PROGRAMS\icon2.jpg")
            self.time_img = pygame.transform.scale(self.time_img, (150,150))
            screen.blit(self.time_img, (self.w/2-75,self.h-140))
            self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time() 
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
             
                
        clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self.reset=False
        self.end = False

        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0


        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        msg = "Word Practice"
        self.draw_text(self.screen, msg,80, 80,self.HEAD_C)  
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)


        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()



Game().run()
