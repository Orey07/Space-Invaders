import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio # type: ignore
from picture import Picture
import constants as cons
import gamewindow as gw

class ene:
    x: float
    y: float
    pic: str

    #intializing the position and picture to be used for enemy
    def __init__(self, x: float, y: float, pic:str):
        self.x = x
        self.y = y
        self.image = Picture(pic)

    #Moves the enemy based on input
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    #Draws the enemy based on image
    def draw(self, w, h):
        stddraw.picture(self.image, self.x, self.y, w, h)

    def draw_scaled(self, size, w, h):
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.picture(self.image, self.x, self.y, w * (size * 2), h * (size*2))


#create backgroud enemies
def bgen(rows: int, cols: int, distance, x_pos: float, y_pos: float, e_pic: str) -> list[ene]:
    d = distance
    enemies = stdarray.create1D(rows * cols, None)
    #intialized all enemies to (None)
    for i in range(rows):
        for j in range(cols):
            x = x_pos + j*d
            y = y_pos - i*d
            enemies[i * cols + j] = ene(x,y,e_pic)
    return enemies

def mbgen(enemies, rows: int, cols: int, vx: float, vy: float):
    
    margin = cons.ENEMY_SIZE/2

    hit_wall = False

    #Made so that all enemies get animated at the same time
    #checks if edge has been reached on each enemy
    for enemy in enemies:
        
        #condition that checks if wall reached
        if (enemy.x + margin) > gw.X_MAX or (enemy.x - margin) < gw.X_MIN:
            hit_wall = True
            break
    
    if hit_wall:

        #changes the horizontal direction when edge reached
        vx = -vx

    #moves all the enemies horizontally based on direction in (vx)
    for enemy in enemies:
        enemy.move(vx, 0)
    
    #draws all the enemies according to the formating in class Enemy
    for enemy in enemies:
        enemy.draw(cons.tw, cons.th)
    
    #returns vx so the horizontal direction can be updated
    return vx

def zoomcen(enemies, rows, cols, step_size, sx, sy):
  
    spacing = 0.55  # space between enemies
    targets = []

    # Assign each enemy its final target position
    for i in range(rows):
        for j in range(cols):
            tx = sx + j * spacing
            ty = sy - i * spacing
            targets.append((tx, ty))

    # Stage 1: Move each enemy to its target position
    for idx, enemy in enumerate(enemies):
        tx, ty = targets[idx]
        while abs(enemy.x - tx) > 0.01 or abs(enemy.y - ty) > 0.01:
            dx = tx - enemy.x
            dy = ty - enemy.y
            length = (dx**2 + dy**2)**0.5
            if length == 0:
                break
            enemy.move(step_size * dx / length, step_size * dy / length)

            stddraw.clear(stddraw.BLACK)
            for e in enemies:
                e.draw(cons.tw, cons.th)
            stddraw.show(0.025)

    # Enemies now at center — begin "marching forward"
    final_size = 0.9  # Final big size
    grow_steps = 50   # Smooth animation frames

    for size_step in range(grow_steps):
        stddraw.clear(stddraw.BLACK)
        scale = (size_step + 1) / grow_steps * final_size
        for enemy in enemies:
            enemy.draw_scaled(scale, cons.tw, cons.th)
        stddraw.show(10)
    stddraw.show(2000)

def showtitle_sc():

    #image1 = Picture("starry1.jpg")
    #image2 = Picture("starry2.jpg")
    #image3 = Picture("starry3.jpg")
    image4 = Picture("Portal.png")
    #frames = [image1, image2, image3]
    #frame_index = 0

    enemies1 = bgen(cons.l1_rows, cons.l1_cols, cons.l1_spacing, 5, 9, "enemy.png")
    #enemies2 = bgen(cons.l1_rows, cons.l1_cols, cons.l1_spacing, 0.8, 1.6, "enemy2.jpg")
    vx = cons.t_vx 

    stddraw.setPenColor(stddraw.WHITE)
    while True:
        stddraw.clear(stddraw.BLACK)
        stddraw.picture(image4, 4.5, 5, 15, 10)

        vx = mbgen(enemies1, cons.l1_rows, cons.l1_cols, vx, 0)
        #vx = mbgen(enemies2, cons.l1_rows, cons.l1_cols, vx, 0)

        # Draw title text on top (unchanging)
        #stddraw.setFontSize(40)
        #stddraw.text(0, 2, "SPACE INVADERS")
        stddraw.picture(Picture("Title.png"), 5, 5, 3, 3)
        stddraw.setFontSize(20)
        stddraw.text(5, 2, "Press SPACE to start...")
        stddraw.show(100)

        #frame_index = (frame_index + 1) % len(frames)

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == ' ':
                break
    
    zoomcen(enemies1, cons.l1_rows, cons.l1_cols, 0.01, 5, 8)
    #zoomcen(enemies2, cons.l1_rows, cons.l1_cols, 0.01, -0.8, 0.8)

    stddraw.clear(stddraw.BLACK)
    stddraw.show(cons.DT)

    

def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(gw.X_MIN, gw.X_MAX)
    stddraw.setYscale(gw.Y_MIN, gw.Y_MAX)
    showtitle_sc() 

if __name__ == "__main__":
    main()
