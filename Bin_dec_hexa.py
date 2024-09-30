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


    # Connaitres le nombre des dizaines pour faire 1 ^0, 0 ^1, 1 ^2, etc ...
    while number_test > 1:
        number_test = round(number_test / 10)
        number_dizaine += 1

    number_test = number
    # Decomposition d'un nombre en liste
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

print(bin_other(11001,2,10))