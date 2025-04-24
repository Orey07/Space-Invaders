import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw
from picture import Picture
from missiles import Missile

shooter_size = 0.5
shooter_speed = 0.2
shooter_dist = 1
angle_change = math.radians(15)


class Shooter:
    def __init__(self, pos_x, pos_y):
        pos_x,pos_y = gw.X_MAX/2, shooter_dist * shooter_size
        self.pos = [pos_x,pos_y]
        self.aim_angle = 90
        self.lives = 3

    def draw(self):
        angle_rad = math.radians(self.shooting_angle)
        pos_x = self.pos[0] + math.cos(angle_rad) * shooter_size
        pos_y = self.pos[1] 
        image_path = Picture('shooter.JPG')  
        stddraw.picture(image_path, pos_x, pos_y, shooter_size/2, shooter_size/2)
        
    def damage(self):
        self.lives = self.lives - 1
        if self.health <= 0:
            gameover()
            
    def shoot(self):
        self.missiles = []
        angle_rad = math.radians(self.shooting_angle)
        vel_x = missile_speed * math.cos(angle_rad)
        vel_y = missile_speed * math.sin(angle_rad)

        self.missiles.append(pos_x,pos_y,vel_x,vel_y)
        shoot_sound.play()

    def input(self):
        global LEFT,RIGHT
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'a':
                LEFT = True
                RIGHT = False
            elif key =='d':
                RIGHT = True
                LEFT = False
            elif key == 's':
                LEFT = False
                RIGHT = False
                
    def update_aim(self, angle_change):
        if 0 < self.aim_angle < math.radians(180):
            self.aim_angle += angle_change
                            
    def update_pos(self,missiles):
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == stddraw.KEY_LEFT:
                pos_x -= shooter_speed
            elif key == stddraw.KEY_RIGHT:
                pos_x += shooter_speed
            elif key == K_LEFT:
                shooter.update_aim(angle_change)
            elif key == K_RIGHT:
                shooter.update_aim(-angle_change)
            elif key == K_SPACE:
                shooter.shoot()
                
        shooter.x = max(shooter_size / 2, min(gw.X_MAX - shooter_size / 2, pos_x))
        shooter.y = shooter_dist*shooter_size
                

      
if __name__ == "__main__":
    main()
