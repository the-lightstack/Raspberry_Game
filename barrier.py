import pygame
pygame.init()

class Barrier:
    def __init__(self,x,y,w,h,var):

        self.rect=pygame.Rect(x,y,w,h)
        self.var=var
        self.var.barriers.append(self)

        self.color=(100,0,100)

    def show(self):
        pygame.draw.rect(self.var.screen,self.color,(self.rect.x-self.var.camera_scrolling.x,self.rect.y-self.var.camera_scrolling.y,self.rect.w,self.rect.h))