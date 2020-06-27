from yoel_engine import * 
from player import *
from enemy import *
from game_world import *


def main():
    
    
    ygame_world = game_world()
    
    yoel_engine.world = ygame_world
    yoel_engine.camera = {'x': 5 , 'y': 0 , 'z': -2 , 'f':1}
  

    
    yoel_engine.init(20)
    
    
main()
