from p5 import *
import random
from playsound import playsound
import threading
import tkinter
import customtkinter

toto = 0
totalRebond = 0

def selectionerVxVyDiamètre():
    global vx, vy, d
    root_tk = tkinter.Tk()
    root_tk.geometry("600x300")
    root_tk.title("Balle rebondissante")

    label = customtkinter.CTkLabel(master=root_tk,text="vitesse horizontale de départ : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.2, rely=0.2, anchor=tkinter.CENTER)
    entry = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    vx =  entry.get()
    vx = int(vx)

    label = customtkinter.CTkLabel(master=root_tk,text="vitesse verticale de départ : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)
    entry1 = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    vy =  entry1.get()
    vy = int(vy)

    label = customtkinter.CTkLabel(master=root_tk,text="diamètre de départ : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    d =  entry2.get()
    d = int(d)

    root_tk.mainloop()

def createCanvas(a,b):# fonction qui crée la fenêtre
    size(a,b)
    no_stroke()

def setup(): 
    global bx,by,vx,vy,d
    d = random.randint(5,20)# commencer avec le rayon du cercle aléatoirement
    bx = random.randint(200, 300)# commnce dans un carré de 100px de côté 
    by = random.randint(150, 250)# avec un centre à 250,200
    selectionerVxVyDiamètre()
    #vx =  # variable vitesse horizontale
    #vy =  # variable vitesse verticale
    createCanvas(500,400) # crée une fenêtre de 500 x 400 pixels

def changerVitesse() : # fonction qui permet d'augmenter la vitesse verticale et horizontale de la balle
    global vx,vy,b
    b = random.randint(90,110)
    vx = vx * (b/100)
    vy = vy * (b/100)

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
        if d == 20 : 
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
        if d == 20 : 
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