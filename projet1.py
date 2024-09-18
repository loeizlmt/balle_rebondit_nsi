from p5 import *
import random



def createCanvas(a,b):
    size(a,b)
    no_stroke()

def setup():
    global bx,by,vx,vy,r
    r = 20
    bx = 50
    by = 50
    vx = 5
    vy = 5
    createCanvas(1000,500) # crée une fenêtre de 1000 x 500 pixels
def draw():# cette fonction s'exécute  en boucle 60 fois par seconde...
    global bx,by,vx,vy,r
    background(0,0,0)# fond noir
    # mouvement du cercle sur l'axe horizontal
    bx = bx + vx
    by = by + vy
    # rebond sur les bords gauche et droit
    if bx < r or bx > 1000 - r:
        vx = -vx
        bx = random.randint(1, 70)
        by = random.randint(1, 70)
    if by < r or by > 500 - r: 
        vy = -vy
        bx = random.randint(1, 70)
        by = random.randint(1, 70)
    # dessin du cercle
    circle(bx,by,2*r)   
    fill(124,125,255) 
run()