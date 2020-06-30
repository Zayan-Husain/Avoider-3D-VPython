from yoel_engine import * 
from player import *
from enemy import *
from game_world import *
from game_over import *


def main():
    
    
    ygame_world = game_world();
    game_over2 = game_over();
    


    yoel_engine.camera = {'x': 5 , 'y': 0 , 'z': -2 , 'f':1}

    yoel_engine.add_world(ygame_world,"game_world");
    yoel_engine.add_world(game_over2, "game_over")

    
    yoel_engine.change_world("game_world");
    
    
    
    yoel_engine.init(20)
    
    
main()
