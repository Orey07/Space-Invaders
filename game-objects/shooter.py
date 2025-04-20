import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

# constants
SHOOTER_SIZE = 0.1
SHOOTER_SPEED = 3

pos_x = gw.X_MAX/2
pos_y = 1


class SHOOTER:
    x : float
    y : float 
    pic : str

    def health_status(self,health, damage):
        self.health = health
        self.health -= damage
         
    def dead(self):
        if self.health < 0:
            return self.health = 0
    
    def alive(self):
        return self.health > 0

def health_bar(shooter):
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledRectangle(1, 9.5, 8, 0.5)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledRectangle(1, 9.5, 8*(shooter.health/100),0.5)

    while True:
        stddraw.health_bar(100)
        stddraw.show()

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'd':
                shooter.health_status(5)
        
        if dead():
            stdio.writeln("Player is dead!")
            break

def draw_shooter(self):
    pic = Picture('shooter')
    stddraw.picture(pic, self.x,self.y)

    
        
def shooter_motion(self, pos_x, pos_y):
    self.x = pos_x
    self.y = pos_y
    
    while True:
        if stddraw.hasNextKeyTyped():
            keys = stddraw.nextKeyTyped()
            if keys == stddraw.K_LEFT:
                pos_x -= SHOOTER_SPEED
            elif keys == stddraw.K_RIGHT:
                pos_x += SHOOTER_SPEED
            elif keys == stddraw.K_DOWN:
                pos_y -= SHOOTER_SPEED
            elif keys == stddraw.K_UP:
                pos_y += SHOOTER_SPEED
            elif keys == stddraw.K_ESCAPE:
                break
            
        # Boundary conditions
        pos_x = max(SHOOTER_SIZE/2,min(gw.X_MAX - SHOOTER_SIZE/2, pos_x))
        pos_y = max(SHOOTER_SIZE/2,min(gw.Y_MAX - SHOOTER_SIZE/2, pos_y))
       
def main():
    
  

if __name__ == "__main__":
    main()
