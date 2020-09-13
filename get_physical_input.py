import pygame
pygame.init()

from gpiozero import Button
class Physical_Button:
    def __init__(self,var):
        self.var=var
        self.button=Button(18)
        self.button.when_pressed=self.assign_jump
    
    def assign_jump(self):
        if self.var.game_started:
            self.var.player.jump=True
        else:
            self.var.game_started=True
        
    
    def check_pressed(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("Hey buddy")
                self.var.player.jump=True
        if self.button.is_pressed:
            print("BAmm")
            self.var.player.jump=True