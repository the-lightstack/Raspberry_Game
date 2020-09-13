import pygame
from get_physical_input import Physical_Button
from player import Player
from barrier import Barrier
from goal import Goal
pygame.init()


def main():
    def level1():
        #game area x is from -100 to 500
        Barrier(-100,800,1000,50,var)#floor
        Barrier(-100,-200,20,1200,var)#left sky pillar
        Barrier(500,-200,20,1200,var)#right sky pillar
        Barrier(-100,690,200,15,var)#first platform
        Barrier(300,580,200,15,var)#second platform right side
        Barrier(-100,490,200,15,var)#third platform
        Barrier(0,380,140,15,var)#next platform on the left side above previous one
        #Barrier(300,360,200,15,var)#another platforom on the right side
        Barrier(300,280,200,15,var)
        Barrier(270,190,130,15,var)
        Barrier(-100,100,200,15,var)#third platform
        
        Barrier(270,0,100,15,var)
        
        #Barrier(160,300,140,15,var)
        #Barrier(60,290,10,15,var)#small nob left side next to platform
        #Barrier(450,270,50,15,var)
        #Barrier(x,y,w,h,var)
        #Barrier(x,y,w,h,var)
        
        var.end=Goal(360,40,10,var)
    class Var:
        def __init__(self):
            self.window_width=1000
            self.window_height=700
            self.FRAME_TITLE="One Button"
            
            self.game_going=True
            self.screen=pygame.display.set_mode((self.window_width,self.window_height))
            pygame.display.set_caption(self.FRAME_TITLE)

            self.barriers=[]
            self.clock=pygame.time.Clock()
            self.FPS=30
            self.player=Player(300,600,self)
            self.won_level=False
            self.camera_scrolling=pygame.Vector2(0,0)
            
            self.game_started=False
    var=Var()
    phys_button=Physical_Button(var)
    

    
    level1()

    while var.game_going:
        #print(var.clock.get_fps())
        #print("len-barriers:",len(var.barriers))
        var.clock.tick(var.FPS)
        var.camera_scrolling.x=var.player.rect.x-var.window_width/2
        var.camera_scrolling.y=var.player.rect.y-var.window_height+200
        #print("mouse:",pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                var.game_going=False
            phys_button.check_pressed(event)
        if not var.won_level:
            var.screen.fill((200,100,220))
        else:
            var.screen.fill((100,200,220))
        pygame.draw.rect(var.screen,(180,80,200),(0,600-var.camera_scrolling.y/10,1200,300))
        for i in var.barriers:
            i.show()
        var.end.update()
        var.player.update()
        
        pygame.display.flip()
if __name__=="__main__":
    main()