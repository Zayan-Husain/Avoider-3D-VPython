from yoel_engine import *
from player import *
from enemy import *
from random import *

############### game_world ##########################################

class game_world(y_world):
    # attributes (properties)
    score = 0;
    score_label = 0;
    spawn_timer = 0;
    def init(self):
        self.remove_all();
        self.spawn_timer = y_timer(40);
        enemy2 = enemy(1, 2, 2, sphere(), 0.05);
        yplayer = player(0,2,1,sphere(),0.5);
        self.score_label = ylabel(10, 0, 0, "Score: " + str(self.score));
        self.add(yplayer) ;
        self.add(enemy2) ;
        self.add(self.score_label);
        
    #end init

    def update(self):
        y_world.update(self);
        self.score += 1;
        self.score_label.stxt("Score: " + str(self.score))
        self.spawn_enemy();
        if self.not_active:
            self.hide_all()
    #end update
    def spawn_enemy(self):
      if self.spawn_timer.finished():
        #        up   down left right forward backward 
        dirs = ["u", "d", "l", "r", "f", "b"];
        _dir = randInt(0, len(dirs) - 1)
        enemyDir = dirs[_dir];
        x = randInt(-10, 10);
        y = randInt(-10, 10);
        z = randInt(-10, 10);
        if enemyDir == "d":
          x = 10
        elif enemyDir == "u":
          x = -10
        elif enemyDir == "l":
          y = 10
        elif enemyDir == "r":
          y = -10;
        elif enemyDir == "f":
          z = 10;
        elif enemyDir == "b":
          z = -10;
        e = enemy(x, y, z, box(), 0.25);
        e.dir = enemyDir
        self.add(e);
    # end spawn_enemy

###############end  game_world ##########################################