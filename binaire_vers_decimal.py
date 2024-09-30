# SUJET : binaire, decimal, hexadecimal vers binaire, deimal, hexadecimal

#        On considere les nombres entiers ecrits en base 2, 10 et 16.
#        Ecrire un programme qui permet de passer de l'ecriture d'un entier dans
#        une des bases (2, 10 ou 16) à l'ecriture de cet entier dans une des bases
#        (2, 10 ou 16).
       
#        Vous serez evalues suivant les 6 criteres decrits dans le fichier excel de nom
#        "notation__projets_nsi__p01_et_p04__2024_2025.xlsx" et qui sont designes par:
 
#        1. Documentation claire
#        2. Lisibilite du code
#        3. Run (execution du programme)
#        4. Presentation (...du projet devant la classe)
#        5. Architecture (organisations des dossiers et fichiers)
#        6. IA generatives (interactions avec les IA generatives)

# REMARQUE : Vous n'utiliserez pas les eventuelles fonctions dejà disponibles dans python,
#        pour passer d'une base à une autre.

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def get_decimal_number():
        user_input = input("Enter a decimal number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a decimal number.")

decimal_number = get_decimal_number()
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")