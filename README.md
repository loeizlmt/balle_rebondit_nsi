Variable 1 :
-La variable "toto" s'incrémente de +1 à chaque fois que la balle atteint un diamètre de 20 pixels. Ce qui permet de vérifier si on doit on non arrêter le programme car quand cette variable contient la valeur 3, le programme s’arrête. 
Variable 2 :
-La variable "total rebond" sert à calculer le nombre de rebond pour l'afficher à la fin.
Fonction 1 :
-La fonction "createCanvas" permet de créer une fenêtre avec les dimension souhaités.
Variable 3 :
-La variable "d" définit le diamètre du cercle.
Variable bx c'est la position de la balle sur l'axe horizontal
Variable by c'est la position de la balle sur l'axe vertical
Variable vx c'est la vitesse horizontale de la balle
Variable vy c'est la vitesse verticale de la balle
Pour ajouter un son on a utilisé la bibliothèque threading qui permet de jouer le son dans un autre thread (un peu comme une sorte de sous-programme) pour éviter d'interrompre le programme car sinon la balle serait bloquée le temps que le son soit joué.
Notre script fonctionne sous python 3.9.19 car p5 ne fonctionnait pas avec les versions plus récentes.
https://www.zonensi.fr/Miscellanees/utilisationP5/
