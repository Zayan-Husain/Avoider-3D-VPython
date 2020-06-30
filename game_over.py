from yoel_engine import *

class game_over(y_world):
  score = 0
  
  def init(self):
    self.remove_all()
    game_world = yoel_engine.get_world("game_world");
    self.score = game_world.score;
    game_over_text = ylabel(9, 0, 0, "Game Over!");
    score = ylabel(3, 0, 0, "Score: " + str(self.score));

    self.add(game_over_text);
    self.add(score);
    
  def update(self):
        y_world.update(self);
   
    #end update
