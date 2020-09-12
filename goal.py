import pygame
pygame.init()

class Goal:
    def __init__(self,x,y,r,var):
        self.rect=pygame.Rect(x,y,r,r)
        self.var=var

    
    def show(self):
        pygame.draw.circle(self.var.screen,(200,40,40),(int(self.rect.x-self.var.camera_scrolling.x),int(self.rect.y-self.var.camera_scrolling.y)),self.rect.w)
    def check_hit(self):
        if self.var.player.rect.colliderect(self.rect):
            self.var.won_level=True

    def update(self):
        self.check_hit()
        self.show()