import crypt
import cs50
import math
import sys


# First we check to see that we have only two arguments: ./crack itself and the hash.
# If the count of arguments (len(sys.argv) is not 2, the program boots the user back to the command line, and gives the usage template.
def crack():
    if len(sys.argv) != 2:
        print("Usage: python crack.py hash")
        return None

    # Can't forget to store the hash, the second argument given by the user.
    hashish = sys.argv[1]

    # Here we pull out the salt from the hash. The salt is the first two characters of the hash.
    # The salt helps the crypt function encrypt a password, and helps us match the hash to the password.
    salt = hashish[:2]

    # This string contains every possible character in our password (in this case, alphabetic + null).
    possibilitiesstr = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    possibilities = list(possibilitiesstr)
    length = len(possibilities)
    key = ["","","","",""]

    # This cascade of for loops iterates over all of the characters in the possiblities string for each place in our key string.
    for n in range(len(possibilities) + 1):
        key[5] = possibilities[n]


        for m in range(len(possibilities) + 1):
            key[4] = possibilities[m]


            for l in range(len(possibilities) + 1):
                key[3] = possibilities[l]


                for k in range(len(possibilities) + 1):
                    key[2] = possibilities[k]


                    for j in range(len(possibilities) + 1):
                        key[1] = possibilities[j]

                        for i in range(len(possibilities) + 1):
                            key[0] = possibilities[i]

                            # When the key, encrypted with the salt via the crypt function, equals the provided hash, the program stops and print the key (aka password).
                            if crypt.crypt(str(key),salt) == hashish:
                                print(str(key))

crack()