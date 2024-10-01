def binary_to_decimal(binary_string):
    decimal = 0
    power = 0
    for digit in reversed(binary_string):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def get_binary_number():
    while True:
        user_input = input("Entrez un nombre binaire (0 ou 1) : ")
        if set(user_input).issubset({"0", "1"}):
            return user_input
        else:
            print("Erreur, le nombre binaire ne doit contenir que des 0 et des 1.")

def binary_to_decimal(binary_string):
    decimal = 0
    power = 0
    for digit in reversed(binary_string):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

binary_number = get_binary_number()
decimal_number = binary_to_decimal(binary_number)
print(f"Le nombre décimal équivalent est : {decimal_number}")