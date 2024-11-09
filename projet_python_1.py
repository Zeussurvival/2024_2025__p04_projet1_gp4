# def binaire_vers_decimal(binaire):
#     decimal = 0
#     for i, bit in enumerate(reversed(binaire)):
#         decimal += int(bit) * (2 ** i)
#     return decimal

# def decimal_vers_binaire(decimal):
#     if decimal == 0:
#         return "0"
#     binaire = ""
#     while decimal > 0:
#         binaire = str(decimal % 2) + binaire
#         decimal //= 2
#     return binaire

# def decimal_vers_hexadecimal(decimal):
#     if decimal == 0:
#         return "0"
#     hexadecimale = ""
#     hex_chars = "0123456789ABCDEF"
#     while decimal > 0:
#         hexadecimale = hex_chars[decimal % 16] + hexadecimale
#         decimal //= 16
#     return hexadecimale

# def hexadecimal_vers_decimal(hexadecimal):
#     decimal = 0
#     hex_chars = "0123456789ABCDEF"
#     for i, char in enumerate(reversed(hexadecimal)):
#         decimal += hex_chars.index(char.upper()) * (16 ** i)
#     return decimal

# def convertir_nombres():
#     print("Choisissez la base d'entrée :")
#     print("1. Binaire (base 2)")
#     print("2. Décimal (base 10)")
#     print("3. Hexadécimal (base 16)")
    
#     choix_entree = input("Votre choix (1/2/3) : ")

#     if choix_entree == "1":
#         nombre_binaire = input("Entrez le nombre en binaire : ")
#         nombre_decimal = binaire_vers_decimal(nombre_binaire)
#     elif choix_entree == "2":
#         nombre_decimal = int(input("Entrez le nombre en décimal : "))
#     elif choix_entree == "3":
#         nombre_hexadecimal = input("Entrez le nombre en hexadécimal : ")
#         nombre_decimal = hexadecimal_vers_decimal(nombre_hexadecimal)
#     else:
#         print("Choix invalide.")
#         return

#     print("\nChoisissez la base de sortie :")
#     print("1. Binaire (base 2)")
#     print("2. Décimal (base 10)")
#     print("3. Hexadécimal (base 16)")
    
#     choix_sortie = input("Votre choix (1/2/3) : ")


#     if choix_sortie == "1":
#         print(f"Le nombre en binaire est : {decimal_vers_binaire(nombre_decimal)}")
#     elif choix_sortie == "2":
#         print(f"Le nombre en décimal est : {nombre_decimal}")
#     elif choix_sortie == "3":
#         print(f"Le nombre en hexadécimal est : {decimal_vers_hexadecimal(nombre_decimal)}")
#     else:
#         print("Choix invalide.")
        

# if __name__ == "__main__":
#     convertir_nombres()

def binaire_vers_decimal(binaire):
    decimal = 0
    for i, bit in enumerate(reversed(binaire)):
        decimal += int(bit) * (2 ** i)
    return decimal

def decimal_vers_binaire(decimal):
    if decimal == 0:
        return "0"
    binaire = ""
    while decimal > 0:
        binaire = str(decimal % 2) + binaire
        decimal //= 2
    return binaire

def decimal_vers_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    hexadecimale = ""
    hex_chars = "0123456789ABCDEF"
    while decimal > 0:
        hexadecimale = hex_chars[decimal % 16] + hexadecimale
        decimal //= 16
    return hexadecimale

def hexadecimal_vers_decimal(hexadecimal):
    decimal = 0
    hex_chars = "0123456789ABCDEF"
    for i, char in enumerate(reversed(hexadecimal)):
        decimal += hex_chars.index(char.upper()) * (16 ** i)
    return decimal

def convertir_nombres():
    while True:
        print("\nChoisissez la base d'entrée :")
        print("1. Binaire (base 2)")
        print("2. Décimal (base 10)")
        print("3. Hexadécimal (base 16)")
        
        choix_entree = input("Votre choix (1/2/3) : ")

        if choix_entree == "1":
            while True:
                nombre_binaire = input("\nEntrez le nombre en binaire : ")
                if all(bit in '01' for bit in nombre_binaire):  # Vérifie si tous les bits sont 0 ou 1
                    nombre_decimal = binaire_vers_decimal(nombre_binaire)
                    break
                else:
                    print("\nEntrée invalide. Veuillez entrer un nombre binaire valide.")
            break
        elif choix_entree == "2":
            while True:
                try:
                    nombre_decimal = int(input("\nEntrez le nombre en décimal : "))
                    break
                except ValueError:
                    print("\nEntrée invalide. Veuillez entrer un nombre décimal valide.")
            break
        elif choix_entree == "3":
            while True:
                nombre_hexadecimal = input("\nEntrez le nombre en hexadécimal : ")
                if all(char in '0123456789ABCDEFabcdef' for char in nombre_hexadecimal):  # Vérifie si tous les caractères sont valides
                    nombre_decimal = hexadecimal_vers_decimal(nombre_hexadecimal)
                    break
                else:
                    print("\nEntrée invalide. Veuillez entrer un nombre hexadécimal valide.")
            break
        else:
            print("\nChoix invalide. Veuillez réessayer.")

    while True:
        print("\nChoisissez la base de sortie :")
        print("1. Binaire (base 2)")
        print("2. Décimal (base 10)")
        print("3. Hexadécimal (base 16)")
        
        choix_sortie = input("Votre choix (1/2/3) : ")

        if choix_sortie == "1":
            print(f"\nLe nombre en binaire est : {decimal_vers_binaire(nombre_decimal)}")
            break
        elif choix_sortie == "2":
            print(f"\nLe nombre en décimal est : {nombre_decimal}")
            break
        elif choix_sortie == "3":
            print(f"\nLe nombre en hexadécimal est : {decimal_vers_hexadecimal(nombre_decimal)}")
            break
        else:
            print("\nChoix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    convertir_nombres()