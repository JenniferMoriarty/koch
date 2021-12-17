import pygame
import math
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (-1800,50)
pygame.init()  #sets up pygame
pygame.display.set_caption("koch")  # sets the window title
screen = pygame.display.set_mode((2000, 1000))  # creates game screen
screen.fill((0,0,0)) #wipe screen black

def drawSnow (lev, x1, y1, x5, y5):
    if lev == 0:
        if lev < 10:
          pygame.draw.line(screen, (level*20, level*10, 200), (x1, y1), (x5, y5), 1)
        else:
          pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x5, y5), 1)  
   
    else:       
        #calculate distance between points
        deltaX = x5 - x1;
        deltaY = y5 - y1;
 
        #cut distance to a third
        x2 = x1 + deltaX / 3;
        y2 = y1 + deltaY / 3;
 
        #calculate placement of new endpoints
        x3 = int(0.5 * (x1+x5) + math.sqrt(3.0) * (y1-y5)/6);
        y3 = int(0.5 * (y1+y5) + math.sqrt(3.0) * (x5-x1)/6);
        x4 = x1 + 2 * deltaX /3;
        y4 = y1 + 2 * deltaY /3;
 
        pygame.display.flip()
        #recursively call itself
        drawSnow(lev-1, x1, y1, x2, y2);
        drawSnow(lev-1, x2, y2, x3, y3);
        drawSnow (lev-1, x3, y3, x4, y4);
        drawSnow (lev-1, x4, y4, x5, y5);
            

#these two variables hold the x and y positions of the square
#initalize these variables to where you want your square to start
square_x = 50;
square_y = 50;
level = 0

while True:
   
    #print("please enter level:");
    #level= int(input());
    level+=1
    #input()
    print(level)


    #drawSnow(level, 80, 1040, 1120, 1040);
    drawSnow(level, 1120, 1040, 600, 0);
    #drawSnow(level, 600, 0, 80, 1040);
    print("done")
    pygame.display.flip()


