from p5 import *
import random

t = 0
rebond=False
rebond1=False
toto = 0
totalRebond = 0


def createCanvas(a,b):# fonction qui crée la fenêtre
    size(a,b)
    no_stroke()

def setup():
    global bx,by,vx,vy,r
    r = random.randint(5,20)
    bx = random.randint(200, 300)
    by = random.randint(150, 250)
    vx = 4
    vy = 5
    createCanvas(500,400) # crée une fenêtre de 1000 x 500 pixels
def draw():# cette fonction s'exécute  en boucle 60 fois par seconde...
    global bx,by,vx,vy,r,t,rebond1,rebond,toto,totalRebond
    background(0,0,0)# fond noir
    # mouvement du cercle sur l'axe horizontal
    bx = bx + vx
    by = by + vy
    # rebond sur les bords gauche et droit
    if bx < r and rebond==False or bx > 500 - r and rebond==False:
        vx = -vx
        vx = (vx * (10/100)) + vx
        vy = (vy * (10/100)) + vy
        r = random.randint(1, 10)#changer le rayon du cercle de manière pseudo aléatoire
        rebond=True
        totalRebond = totalRebond +1
        if r == 10 : 
            toto = toto + 1
    if by < r and rebond1 == False or by > 400 - r and rebond1 == False: 
        vy = -vy
        vx = (vx * (10/100)) + vx
        vy = (vy * (10/100)) + vy
        r = random.randint(1, 10)#changer le rayon du cercle de manière pseudo aléatoire
        rebond1=True
        totalRebond = totalRebond +1
        if r == 10 : 
            toto = toto + 1
    if t > 60 :
        rebond=False
        rebond1=False
        t = 0

    if toto == 3 or toto > 3 :
        print(f"la balle à rebondit {totalRebond} fois")
        exit()
    # dessin du cercle
    circle(bx,by,2*r)   
    fill(124,125,255)
    t = t + 1
run()