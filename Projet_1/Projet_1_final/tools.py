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

def cool_text(number):
    if number == 1:
        text = "        \/            \/          \/                    \/     \/     \/               "
        print(" _________                                   __   __                                    ")
        print(" \_   ___ \  ____   _______  __ ____________/  |_|__| ______ ______ ____  __ _________ ")
        print("/    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\  |/  ___//  ___// __ \|  |  \_  __ \ ")
        print("\     \___|  <_> |   |  \   /\  ___/|  | \/|  | |  |\___ \ \___ \\  ___/|  |  /|  | \/ ")
        print(" \______  /\____/|___|  /\_/  \___  >__|   |__| |__/____  >____  >\___  >____/ |__|    ")
        return text
    else:
        text = " \____/\___/|_| |_|\_/ \___|_|   \__|_|___/___/\___|\__,_|_|   "
        print(" _____                           _   _                         ")
        print("/  __ \                         | | (_)                        ")
        print("| /  \/ ___  _ ____   _____ _ __| |_ _ ___ ___  ___ _   _ _ __ ")
        print("| |    / _ \| '_ \ \ / / _ \ '__| __| / __/ __|/ _ \ | | | '__|")
        print("| \__/\ (_) | | | \ V /  __/ |  | |_| \__ \__ \  __/ |_| | |   ")
        return text