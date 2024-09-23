from data import *

# Ecrire une fonction python qui prend en entrée une chaine 
# de caractères, et qui renvoie le nombre de caractères de
# cette chaine (PUFS).

def count_characters (chain):
    cpt = 0
    for c in chain:
        cpt = cpt + 1 # on incrémente le compteur de 1
    return cpt

assert count_characters ("salut") == 5
assert count_characters ("salut toi") == 9
assert count_characters ("") == 0

# Ecrire une fonction python qui prend en entrée deux paramètres:
#   - une chaine de caractères de nom chain,
#   - un caractère de nom char,
# et qui renvoie le nombre d'occurence de char dans chain.  (PUFS

def count_occurences_char_in_chain (char, chain):
    cpt = 0
    for c in chain:
        if char == c:
             cpt = cpt + 1
    return cpt

assert count_occurences_char_in_chain ("a", "salut") == 1
assert count_occurences_char_in_chain ("a", "toto") == 0

# Ecrire une fonction python qui prend en entrée une chaine de caractères
# de nom chain, qui ne contient que des voyelles ou des consonnes, et qui 
# renvoie deux listes. 
#   - L'une contiendra les voyelles contenues dans chain,
#   - l'autre les consonnes contenues dans chain.  (PUFS)

from data import voyelles

def etre_voyelle (c):
    return c in voyelles

def faire_voyelles_et_consonnes (chain):
    """
    chain ne contient qu'un sous-ensemble 
    parmi les 26 caractères de l'alphabet,
    en miniscule
    """
    hors_voyelles, hors_consonnes = [],[]
    for c in chain:
        if etre_voyelle (c):
            hors_voyelles.append (c)
        else:
            hors_consonnes.append (c)
    return hors_voyelles, hors_consonnes


assert faire_voyelles_et_consonnes ("saluttoi") == \
    (["a","u","o","i"], ["s","l","t","t"])

# Ecrire un programme python qui prend en entrée une chaine de caractère chain,
# et qui permet de réaliser la tâche suivante:
#   - on demande à l'utilisateur de rentrer la chaine chain,
#   - s'il rentre la bonne chaine alors on affiche un texte de remerciement,
#   - s'il ne rentre pas exactement la chaine attendue alors on lui demande
#     de réessayer...Jusqu'à ce qu'il rentre la bonne chaine. (PUFS)

def ask_for_required_chain (required_chain):
    # user_chain = input (ask_required_chain_text)
    # not_correct = True
    # while not_correct:
    #     if user_chain == required_chain:
    #         print (thank_you_text)
    #         not_correct = False
    #     else:
    #         user_chain = input (ask_again_required_chain_text)          
    user_chain = input ("ask_again_required_chain_text")
    while user_chain != required_chain:
        user_chain = input ("ask_again_required_chain_text")
    print (thank_you_text)

# chain_attendue = "Tom est gay"

# while True:
#     chain = input("Entrez la chaine : ")
#     if chain == chain_attendue:
#         print("Merci ! Vous avez entré la bonne chaine.")
#         break
#     else:
#         print("Erreur, veuillez réessayer.")