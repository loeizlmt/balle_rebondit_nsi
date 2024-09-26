from p5 import *
import random
from playsound import playsound
import threading


toto = 0
totalRebond = 0

def createCanvas(a,b):# fonction qui crée la fenêtre
    size(a,b)
    no_stroke()

def setup(): 
    global bx,by,vx,vy,d
    d = random.randint(5,20)# commencer avec le rayon du cercle aléatoirement
    bx = random.randint(200, 300)# commnce dans un carré de 100px de côté 
    by = random.randint(150, 250)# avec un centre à 250,200
    vx = 4 # variable vitesse horizontale
    vy = 5 # variable vitesse verticale
    createCanvas(500,400) # crée une fenêtre de 500 x 400 pixels

def changerVitesse() : # fonction qui permet d'augmenter la vitesse verticale et horizontale de la balle
    global vx,vy
    vx = (vx * (10/100)) + vx
    vy = (vy * (10/100)) + vy

def changerTaille():# fonction qui permet de changer la taille de la balle aléatoirement
    global d
    d = random.randint(5, 20)# changer le rayon du cercle aléatoirement

def draw():# cette fonction s'exécute  en boucle 60 fois par seconde...
    global bx,by,vx,vy,d,toto,totalRebond
    background(0,0,0)# fond noir
    # mouvement du cercle sur l'axe horizontal
    bx = bx + vx
    by = by + vy # mouvement du cercle sur l'axe vertical

    # rebond sur les bords gauche et droit
    if bx < d or bx > 500 - d:
        threading.Thread(target=lambda: playsound("C://Users//loloj//OneDrive//Bureau//boing.mp3"), daemon=True).start()# ajoute un son qui s'exécute dans un autre thread 
        vx = - vx # inverse la vitesse
        changerVitesse()# fonction qui augmente la vitesse
        changerTaille() # fonction qui change la taille
        totalRebond = totalRebond +1 # permet de compter les rebonds

        # test si le diamètre est égal à 20 et incrémente la variable toto
        if d == 10 : 
            toto = toto + 1

        # si la balle rebondit sur le bord gauche on la replace à bx + d
        if bx < d :
            bx = bx + d

        # si la balle rebondit sur le bord droit on la replace à bx - d
        if bx > 500 - d :
            bx = bx - d   

    # rebond sur les bords haut et bas
    if by < d or by > 400 - d:
        threading.Thread(target=lambda: playsound("C://Users//loloj//OneDrive//Bureau//boing.mp3"), daemon=True).start()# ajoute un son qui s'exécute dans un autre thread 
        vy = -vy # inverse la vitesse
        changerVitesse()# fonction qui augmente la vitesse
        changerTaille() # fonction qui change la taille
        totalRebond = totalRebond +1 # permet de compter les rebonds

        # test si le diamètre est égal à 20 et incrémente la variable toto
        if d == 10 : 
            toto = toto + 1

        # si la balle rebond en haut on la replace à by + d
        if by < d :
            by = by + d # replace la balle pour éviter que la balle rebondisse à l'infini sur le côté

        # si la balle rebond en bas on la replace à by - d
        if by > 400 - d :
            by = by - d # replace la balle pour éviter que la balle rebondisse à l'infini sur le côté

    # vérifie si le diamètre de la balle a été de 20px 3 fois 
    if toto == 3 or toto > 3 :
        print(f"la balle à rebondit {totalRebond} fois") # écrit le nombre total de rebond 
        exit() # arrête le programme

    # dessin du cercle
    circle(bx,by,d)   
    fill(124,125,255) # couleur du cercle
run()