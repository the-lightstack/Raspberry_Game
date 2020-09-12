import pygame
pygame.init()

class Player:
    def __init__(self,x,y,var):
        
        self.start_pos=pygame.Vector2(x,y)
        self.rect=pygame.Rect(x,y,32,64)
        self.var=var
        self.in_air=True
        self.jump=False

        self.color=(0,0,0)

        self.movement_velocity=pygame.Vector2(-2,0)
        self.gravity=-0.1
        self.dead=False
    def update(self):
        self.update_pos()
        self.show()
        self.check_below_level()


    def show(self):
      
        pygame.draw.rect(self.var.screen,self.color,(self.rect.x-self.var.camera_scrolling.x,self.rect.y-self.var.camera_scrolling.y,self.rect.w,self.rect.h))

    def update_pos(self):
        #print("x-vel:",self.movement_velocity.x)
        #print("in-air:",self.in_air)
        if self.in_air:
            self.movement_velocity.y-=self.gravity
        elif not self.in_air and not self.jump:
            self.movement_velocity.y=1
        if self.jump==True and not self.in_air:
            self.movement_velocity.y-=5
            self.in_air=True
            self.jump=False
    
        any_collision=False
        
        self.rect.x+=self.movement_velocity.x
        collisions=self.check_collision()
        
        for i in collisions:
            if self.movement_velocity.x<0:#moving left
                self.movement_velocity.x=self.movement_velocity.x*-1
                self.rect.left=i.rect.right
                any_collision=True
               
            elif self.movement_velocity.x>0:#moving right
                self.movement_velocity.x=self.movement_velocity.x*-1
                self.rect.right=i.rect.left
                
                
                any_collision=True
           

        self.rect.y+=self.movement_velocity.y
        collisions=self.check_collision()
        
        for i in collisions:
           
            if self.movement_velocity.y>0:
                self.rect.bottom=i.rect.top
                self.in_air=False
                any_collision=True
                self.jump=False
               
            if self.movement_velocity.y<0:
                self.rect.top=i.rect.bottom
                any_collision=True
       
        #print("Colliding:",any_collision)
        if not any_collision:
            self.in_air=True
            
    
    def check_collision(self):
        collision_list=[]
        for i in self.var.barriers:
            if self.rect.colliderect(i.rect):
                collision_list.append(i)
        return collision_list
        
    def check_below_level(self):
        if self.rect.y>1400:
            self.dead=True
        elif self.rect.y>1000:
            self.color=(255,0,10)
        
        if self.dead==True:
            self.rect.x=self.start_pos.x
            self.rect.y=self.start_pos.y
            self.movement_velocity.y=-2
            
            self.color=(0,0,0)
            self.dead=False