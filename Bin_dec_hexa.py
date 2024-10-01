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


print()

def reverse_chain(chain):
    reversed_chain = ""
    for c in chain:
        reversed_chain = c + reversed_chain
    return reversed_chain

# Pour les fonctions
def convertisseur_bin_hex_to_dec(string,base):
    # binaire d'abord
    chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    number = 0
    trouver = False
    if base == 2:
        for i in range(len(string)):
            if string[i] == "1":
                number += 2 ** i
    
    # if base == 16:
    #     string = reverse_chain(string)
    #     for i in range(len(string)):
    #         for a in range(len(chars)):
    #             print(number,a,i)
    #             if string[i] == chars[a]:
    #                 print(number + a ** i)
    #                 number += a ** i
    if base == 16:
        string_fin = reverse_chain(string)
        for str in range(len(string_fin)):
            while trouver == False:
                for char in range(len(chars)):
                    if string_fin[str] == chars[char]:
                        print(char,str)
                        number += char * (16**str)
                        print(number)
                        trouver = False
                trouver = True
            trouver = False


    return number

print(convertisseur_bin_hex_to_dec("ba",16))



# bin_other est une fonction qui passe du binaire aux autres bases
# def bin_other(number,base_ori,base_fin):
#     # Variables necessaires (todo: a expliquer l'utilité)

#     decompostion_l = []
#     number_finale = ""
#     number_test = number
#     number_quon_regarde = number
#     number_dizaine = 0
#     number = f"{number}"

#     if base_ori == base_fin:
#         return number


#     # Decomposition d'un nombre en liste qui est en base 2 ou en base 10
#     number_test = number
#     for i in number:
#         decompostion_l.append(i)
#     print(decompostion_l)


#     if base_ori == 2:
#         if base_fin == 10:
#             for i in range(len(decompostion_l)):
#                 number_finale += decompostion_l[i] * (2 **i)
#                 print(decompostion_l[i] * (2 ** i),i)
            
#         # elif base_fin == 16:

#     elif base_ori == 10:
#         if base_fin == 2:
#             while number_test > 1:
#                 if number_test % 2 == 0:
#                     number_finale += "0"
#                     number_test /= 2
#                 else:
#                     number_finale += "1"
#                     number_test /= 2


        
#     #     elif base_fin == 16:
    
#     # elif base_ori == 16:
#     #     if base_fin == 2:

#     #     elif base_fin == 10:

#     return number_finale

# print(bin_other(10101,2,10))