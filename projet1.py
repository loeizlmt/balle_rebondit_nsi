from p5 import *

def setup():
    global bx,by,vx,vy,r
    r = 20
    bx = 50
    by = 50
    vx = 23
    vy = 13
    createCanvas(1000,500) # crée une fenêtre de 200 x 200 pixels
def draw():# cette fonction s'exécute  en boucle 60 fois par seconde...
    global bx,by,vx,vy,r
    background(0,0,0)# fond noir
    # mouvement du cercle sur l'axe horizontal
    bx = bx + vx
    by = by + vy
    # rebond sur les bords gauche et droit
    if bx < r or bx > 1000 - r:
        vx = -vx
        fill(random(255),random(255),random(255))
    if by < r or by > 500 - r: 
        vy = -vy
        fill(random(255),random(255),random(255))
    # dessin du cercle
    circle(bx,by,2*r)    
run()