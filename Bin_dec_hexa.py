# Pour les fonctions

# bin_other est une fonction qui passe du binaire aux autres bases
def bin_other(number,base_ori,base_fin):
    number_fin = 0
    number_test = number
    number_dizaine = 0
    if base_ori == base_fin:
        return number
    
    while number_test > 1:
        number_test = round(number_test / 10)
        number_dizaine += 1
        
    if base_ori == 2:
        if base_fin == 10:

            print(number_dizaine)
            
        #if base_fin == 16:

    # if base_ori == 10:
    #     if base_fin == 2:
        
    #     if base_fin == 16:
    
    # if base_ori == 16:
    #     if base_fin == 2:

    #     if base_fin == 10:
print(bin_other(101,2,10))