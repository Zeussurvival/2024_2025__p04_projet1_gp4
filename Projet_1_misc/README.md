Groupe : Emil, Adam, Maxence
followed by Jim Pioche

- _Ce projet a pour but de convertir un nombre binaire, décimal ou héxadécimal en un nombre bianire, décimal ou héxadécimal._

- _Ce projet a été fait dans le but d'un projet de NSI de première._
 
Le fichier "projet_python_final" contient les 2 fichiers python nécessaire au lancement du programme:
  - Un programme python nommé "tools.py" qui va contenir les différentes fonction nécéssaire a la convertion des nombres et pour l'affichage du tag.
  - Un programme python nommé " __main __.py" qui ne contient rien de particulier a part le fait qu'il lance la fonction convertir a chaque fin de celle-ci.

Le programme tools.py contient 2 groupes de fonctions:
 - Les convertisseurs brut:
   
   -> Binaire_decimal(), decimal_binaire() et hexadecimal_decimal(), decimal_hexadecimal()
   
   -> Pour passer du binaire au hexadecimal on converti le nombre binaire en decimal des qu'on l'obtient pour le transformer du decimal au hexadecimal
 - Les affichages:
   
   -> La fonction convertir_nombres() s'occupent de (presque) tout l'affichage et s'occupent de vérifier si les entrées sont correct sinon renvoie un message d'erreur et continue le programme
   
   -> Les fonctions cool_text1() et cool_text2() s'occupent de l'affichage du tag

Le programme __main __.py contient une seule chose:
  - Une boucle qui relance le convertisseur
