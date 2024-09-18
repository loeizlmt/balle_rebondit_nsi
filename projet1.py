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
        r = random.randint(1, 100)#changer le rayon du cercle de manière pseudo aléatoire
    if by < r or by > 500 - r: 
        vy = -vy
        r = random.randint(1, 100)#changer le rayon du cercle de manière pseudo aléatoire
    # dessin du cercle
    circle(bx,by,2*r)   
    fill(124,125,255) 
run()