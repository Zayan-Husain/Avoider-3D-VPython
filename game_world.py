from yoel_engine import *
from player import *
from enemy import *

############### game_world ##########################################

class game_world(y_world):
    # attributes (properties)
    score = 0;
    def init(self):
        yplayer = player(0,2,1,sphere(),0.5)
        yenemy = enemy(0,2,-25,box(),0.5)
        self.add(yplayer) 
        self.add(yenemy) 
    #end init

    def update(self):
        y_world.update(self)
    #end update

###############end  game_world ##########################################