from p5 import *
import random
from playsound import playsound
import threading
import tkinter
import customtkinter
from tkinter import messagebox

toto = 0
totalRebond = 0

# fonction qui permet à l'utilisateur de choisir la vitesse verticale et horizontale
# ainsi que le diamètre de la balle de départ dans une interface graphique avec customtkinter
def selectionerVxVyDiamètre():
    global vx, vy, d,entry,entry1,entry2 # récupère les variables globales
    # fonction qui permet de récupérer les données des entrées et de fermer la fenêtre
    def valider():
        global vx,vy,d # récupère les variables globales
        vx =  entry.get() # récupère la valeur saisie par l'utilisateur et la met dans la bonne variable
        vy =  entry1.get() # récupère la valeur saisie par l'utilisateur et la met dans la bonne variable
        d =  entry2.get() # récupère la valeur saisie par l'utilisateur et la met dans la bonne variable3
        # gère les exceptions pour éviter d'avoir des variables vides
        if vx == ""  or vy == "" or  d == "" :
            messagebox.showerror("ERREUR","Veuillez entrer des valeurs valides")
            root_tk.destroy()
            exit()
        # transforme d,vx et vy en entier.
        d = int(d)
        vy = int(vy)
        vx = int(vx)
        # gère les exceptions pour éviter d'avoir des valeurs trop grandes ou négatives
        if vx > 20 or vx <= 0 or vy > 20 or vy <= 0 or d > 20 or d <= 0 :
            messagebox.showerror("ERREUR","Veuillez entrer des valeurs valides")
            root_tk.destroy()
            exit()
        root_tk.destroy() # ferme la fenêtre

    root_tk = tkinter.Tk()
    root_tk.geometry("600x300")# dimensions de la fenêtre
    root_tk.title("Balle rebondissante")# titre de la fenêtre
    # texte qui indique la valeur à mettre dans la case
    label = customtkinter.CTkLabel(master=root_tk,text="vitesse horizontale de départ (entre 0 et 20) : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
    # entrée où l'utilisateur peut saisir la valeur de la vitesse horizontale de départ
    entry = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)
    # texte qui indique la valeur à mettre dans la case
    label = customtkinter.CTkLabel(master=root_tk,text="vitesse verticale de départ (entre 0 et 20) : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
    # entrée où l'utilisateur peut saisir la valeur de la vitesse verticale de départ
    entry1 = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry1.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)
    # texte qui indique la valeur à mettre dans la case
    label = customtkinter.CTkLabel(master=root_tk,text="diamètre de départ (entre 0 et 20) : ",width=120,height=25,corner_radius=8)
    label.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
    # entrée où l'utilisateur peut saisir la valeur du diamètre de la balle de départ
    entry2 = customtkinter.CTkEntry(master=root_tk,width=120,height=25,corner_radius=10)
    entry2.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
    # bouton pour valider les résultats
    button = customtkinter.CTkButton(master=root_tk,text="Valider",command=valider,width=120, height=32,border_width=0,corner_radius=8)
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    # crée la fenêtre
    root_tk.mainloop()

def createCanvas(a,b):# fonction qui crée la fenêtre
    size(a,b)
    no_stroke()

def setup(): 
    global bx,by,vx,vy,d # récupère les variables globales
    selectionerVxVyDiamètre()# appel de la fonction qui ouvre une interface utilisateur.
    bx = random.randint(200, 300)# commnce dans un carré de 100px de côté 
    by = random.randint(150, 250)# avec un centre à 250,200
    createCanvas(500,400) # crée une fenêtre de 500 x 400 pixels

def changerVitesse() : # fonction qui permet d'augmenter la vitesse verticale et horizontale de la balle
    global vx,vy,b # récupère les variables globales
    b = random.randint(90,110)
    vx = vx * (b/100)
    vy = vy * (b/100)

def changerTaille():# fonction qui permet de changer la taille de la balle aléatoirement
    global d # récupère les variables globales
    d = random.randint(5, 20)# changer le rayon du cercle aléatoirement

def draw():# cette fonction s'exécute  en boucle 60 fois par seconde...
    global bx,by,vx,vy,d,toto,totalRebond # récupère les variables globales
    background(0,0,0)# fond noir
    # mouvement du cercle sur l'axe horizontal
    bx = bx + vx
    by = by + vy # mouvement du cercle sur l'axe vertical

    # rebond sur les bords gauche et droit
    if bx < d/2 or bx > 500 - d/2:
        threading.Thread(target=lambda: playsound("C://Users//loloj//OneDrive//Bureau//boing.mp3"), daemon=True).start()# ajoute un son qui s'exécute dans un autre thread 
        vx = - vx # inverse la vitesse
        changerVitesse()# fonction qui augmente la vitesse
        changerTaille() # fonction qui change la taille
        totalRebond = totalRebond +1 # permet de compter les rebonds

        # test si le diamètre est égal à 20 et incrémente la variable toto
        if d == 20 : 
            toto = toto + 1

        # si la balle rebondit sur le bord gauche on la replace à bx + d/2
        if bx < d/2 :
            bx = bx + d/2

        # si la balle rebondit sur le bord droit on la replace à bx - d/2
        if bx > 500 - d/2 :
            bx = bx - d/2   

    # rebond sur les bords haut et bas
    if by < d/2 or by > 400 - d/2:
        threading.Thread(target=lambda: playsound("C://Users//loloj//OneDrive//Bureau//boing.mp3"), daemon=True).start()# ajoute un son qui s'exécute dans un autre thread 
        vy = -vy # inverse la vitesse
        changerVitesse()# fonction qui augmente la vitesse
        changerTaille() # fonction qui change la taille
        totalRebond = totalRebond +1 # permet de compter les rebonds

        # test si le diamètre est égal à 20 et incrémente la variable toto
        if d == 20 : 
            toto = toto + 1

        # si la balle rebond en haut on la replace à by + d/2
        if by < d/2 :
            by = by + d/2 # replace la balle pour éviter que la balle rebondisse à l'infini sur le côté

        # si la balle rebond en bas on la replace à by - d/2
        if by > 400 - d/2 :
            by = by - d/2 # replace la balle pour éviter que la balle rebondisse à l'infini sur le côté

    # vérifie si le diamètre de la balle a été de 20px 3 fois 
    if toto == 3 or toto > 3 :
        print(f"la balle à rebondit {totalRebond} fois") # écrit le nombre total de rebond 
        exit() # arrête le programme

    # dessin du cercle
    circle(bx,by,d)   
    fill(124,125,255) # couleur du cercle
run()