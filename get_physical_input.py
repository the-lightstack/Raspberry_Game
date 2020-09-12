import pygame
pygame.init()

class Physical_Button:
    def __init__(self,var):
        self.var=var

    def check_pressed(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("Hey buddy")
                self.var.player.jump=True