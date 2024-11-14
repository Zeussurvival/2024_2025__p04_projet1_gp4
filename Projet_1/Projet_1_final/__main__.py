from tools import *

def convertir_nombres():
    while True:
        print("\nChoisissez la base d'entrée :")
        print("1. Binaire (base 2)")
        print("2. Décimal (base 10)")
        print("3. Hexadécimal (base 16)")
        
        choix_entree = input("Votre choix (1/2/3) : ")

        if choix_entree == "1":
            while True:
                nombre_binaire = input("Entrez le nombre en binaire : ")
                if all(bit in '01' for bit in nombre_binaire):  # Vérifie si tous les bits sont 0 ou 1
                    nombre_decimal = binaire_vers_decimal(nombre_binaire)
                    break
                else:
                    print("\nEntrée invalide. Veuillez entrer un nombre binaire valide.")
            break
        elif choix_entree == "2":
            while True:
                try:
                    nombre_decimal = int(input("Entrez le nombre en décimal : "))
                    break
                except ValueError:
                    print("\nEntrée invalide. Veuillez entrer un nombre décimal valide.")
            break
        elif choix_entree == "3":
            while True:
                nombre_hexadecimal = input("Entrez le nombre en hexadécimal : ")
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

def Convertisseur_infini():
    while True:
        convertir_nombres()
        print("\n\n\n")
        print(cool_text1())
        print("\n\n")

#  _____                           _   _                         
# /  __ \                         | | (_)                        
# | /  \/ ___  _ ____   _____ _ __| |_ _ ___ ___  ___ _   _ _ __ 
# | |    / _ \| '_ \ \ / / _ \ '__| __| / __/ __|/ _ \ | | | '__|
# | \__/\ (_) | | | \ V /  __/ |  | |_| \__ \__ \  __/ |_| | |   
#  \____/\___/|_| |_|\_/ \___|_|   \__|_|___/___/\___|\__,_|_|   
                                                               
# _________                                   __   __                                   
# \_   ___ \  ____   _______  __ ____________/  |_|__| ______ ______ ____  __ _________ 
# /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\  |/  ___//  ___// __ \|  |  \_  __ \
# \     \___|  <_> |   |  \   /\  ___/|  | \/|  | |  |\___ \ \___ \\  ___/|  |  /|  | \/
#  \______  /\____/|___|  /\_/  \___  >__|   |__| |__/____  >____  >\___  >____/ |__|   
#         \/            \/          \/                    \/     \/     \/              


if __name__ == "__main__":
    print(cool_text1())
    Convertisseur_infini()