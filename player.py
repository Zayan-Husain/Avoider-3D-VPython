from yoel_engine import *

############### player ##########################################

class player(y_entity):
    # attributes (properties)
    y_type = "player"

    
   
    def update(self):
        y_entity.update(self)
        self.move()
        self.wall_loop()
        self.colide_enemy()
    #end update
        
    def move(self):

        speed = self.speed

        #up
        if y_input.get_key_down("up"):
            y_entity.move_by(self,0,0,-speed)
        #down
        if y_input.get_key_down("down"):
            y_entity.move_by(self,0,0,speed)
        #right
        if y_input.get_key_down("right"):
            y_entity.move_by(self,0,-speed,0)
        #down
        if y_input.get_key_down("left"): 
            y_entity.move_by(self,0,speed,0)
        if y_input.get_key_down("a"):
            y_entity.move_by(self,speed,0,0)
        if y_input.get_key_down("z"):
            y_entity.move_by(self,-speed,0,0)
    #end move#   

            
    def wall_loop(self):
        
        if self.y > 10 :
              self.y =  10;
        if self.y < -10 :
              self.y = -10;
        if self.z > 8 :
              self.z = 8;
        if self.z < -20 :
              self.z = -20;
        if (self.x > 10):
          self.x = 10;
        if (self.x < 0):
          self.x = 0;
    #end wall_loop#


    def colide_enemy(self):
        world = yoel_engine.world ;
        enemy = y_entity.collide(self,"enemy")
    #return
        if enemy:
            yoel_engine.change_world("game_over");
   #end colide_stick

########################end player##################################
            
 
