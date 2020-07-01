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
      self.checkDistance(self.get_by_type("player")[0]);
    # end update
    def wall_loop(self):
      s = self;
      if self.y > 20:
        self.y = -20;
        s.randomize("x");
        s.randomize("z");
      elif self.y < -20:
        self.y = 20;
        s.randomize("x");
        s.randomize("z");
      elif self.x < -20:
        self.x = 20;
        s.randomize("y");
        s.randomize("z");
      elif self.x > 20:
        self.x = -20;
        s.randomize("y");
        s.randomize("z");
      elif self.z < -20:
        self.z = 20;
        s.randomize("x");
        s.randomize("y");
      elif self.z > 20:
        self.z = -20;
        s.randomize("x");
        s.randomize("y");

    def randomize(self, w):
      setattr(self, w, randInt(-10, 10));
      
    def checkDistance(self, obj):
      delta = (self.x - obj.x) + (self.y - obj.y) + (self.z - obj.z);
      if (delta<0):
        return;
      dist = sqrt(delta);
      if dist < 1.5:
        self.grafic.color = color.red;
      else:
        self.grafic.color = color.white;

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