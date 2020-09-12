import pygame
from get_physical_input import Physical_Button
from player import Player
from barrier import Barrier
from goal import Goal
pygame.init()


def main():

    class Var:
        def __init__(self):
            self.window_width=1200
            self.window_height=800
            self.FRAME_TITLE="One Button"
            
            self.game_going=True
            self.screen=pygame.display.set_mode((self.window_width,self.window_height))
            pygame.display.set_caption(self.FRAME_TITLE)

            self.barriers=[]
            
            self.player=Player(300,500,self)
            self.won_level=False
            self.camera_scrolling=pygame.Vector2(0,0)
    var=Var()
    phys_button=Physical_Button(var)
    

    test_barrier=Barrier(0,750,1200,50,var)
    test_barrier2=Barrier(100,200,70,600,var)
    test_barrier3=Barrier(750,50,50,500,var)
    box=Barrier(300,700,70,100,var)
    end=Goal(500,700,10,var)


    while var.game_going:
        var.camera_scrolling.x=var.player.rect.x-var.window_width/2
        var.camera_scrolling.y=var.player.rect.y-var.window_height+200
        print("mouse:",pygame.mouse.get_pos())
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
        end.update()
        var.player.update()
        
        pygame.display.flip()
if __name__=="__main__":
    main()