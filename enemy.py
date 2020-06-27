from yoel_engine import *

############### enemy ##########################################

class enemy(y_entity):
    # attributes (properties)
    y_type = "enemy"
    dir = "f";
    
    def update(self):
      y_entity.update(self);
      self.move();
      self.wall_loop();
    # end update
    def wall_loop(self):
      if self.y > 20:
        self.y = -20;
      elif self.y < -20:
        self.y = 20;
      elif self.x < -20:
        self.x = 20;
      elif self.x > 20:
        self.x = -20;
      elif self.z < -20:
        self.z = 20;
      elif self.z > 20:
        self.z = -20;
      

    def move(self):
      d = self.dir;
      s = self.speed;
      if (d == "f"):
        y_entity.move_by(self, 0, 0, -s);
      if (d == "b"):
        y_entity.move_by(self, 0, 0, s);
      if (d == "u"):
        y_entity.move_by(self, s, 0, 0);
      if (d == "d"):
        y_entity.move_by(self, -s, 0, 0);
      if (d == "l"):
        y_entity.move_by(self, 0, s, 0);
      if (d == "r"):
        y_entity.move_by(self, 0, -s, 0);


###############end enemy ##########################################