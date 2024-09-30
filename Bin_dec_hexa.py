# Truc chat gpt a voir
# def decompose_to_powers_of_10(n):
#     powers = []
#     place_value = 1
#     while n > 0:
#         digit = n % 10
#         if digit > 0:
#             powers.append((digit, place_value))
#         n //= 10
#         place_value *= 10
#     return powers

# def main():
#     try:
#         number = int(input("Enter a number to decompose: "))
#         if number < 0:
#             print("Please enter a non-negative integer.")
#             return
#         decomposition = decompose_to_powers_of_10(number)
#         print(f"The decomposition of {number} into powers of 10 is:")
#         for digit, power in reversed(decomposition):
#             print(f"{digit} * 10^{int(power // 10)}")  # Correctly represents powers of 10
#     except ValueError:
#         print("Invalid input. Please enter a non-negative integer.")

# if __name__ == "__main__":
#     main()

# Pour les fonctions


# bin_other est une fonction qui passe du binaire aux autres bases
def bin_other(number,base_ori,base_fin):
    # Variables necessaires (todo: a expliquer l'utilité)

    decompostion_l = []
    number_finale = 0
    number_test = number
    number_quon_regarde = number
    number_dizaine = 0
    if base_ori == base_fin:
        return number


    # Decomposition d'un nombre en liste qui est en base 2 ou en base 10
    if base_ori == 2 or base_fin == 10:
        number_test = number
        for i in range(number_dizaine + 1):
            number_quon_regarde = number_test % 10
            number_test //= 10
            decompostion_l.append(number_quon_regarde)
        print(decompostion_l)


    if base_ori == 2:
        if base_fin == 10:
            for i in range(len(decompostion_l)):
                number_finale += decompostion_l[i] * (2 **i)
                print(decompostion_l[i] * (2 ** i),i)
            
        # if base_fin == 16:

    # if base_ori == 10:
    #     if base_fin == 2:
        
    #     if base_fin == 16:
    
    # if base_ori == 16:
    #     if base_fin == 2:

    #     if base_fin == 10:

    return number_finale

print(bin_other(10101,2,10))