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

    # This cascade of for loops iterates over all of the characters in the possiblities string for each place in our key string.
    for n in possibilitiesstr:

        for m in possibilitiesstr:

            for l in possibilitiesstr:

                for k in possibilitiesstr:

                    for j in possibilitiesstr:

                        # One of the great things about Python: we can create a string whose characters are iteratively replaced using the {j} notation and the f prefix.
                        # Additionally, .strip() serves to remove white space from the password.
                        pw = f"{j}{k}{l}{m}{n}".strip()

                        # When the key, encrypted with the salt via the crypt function, equals the provided hash, the program stops and print the key (aka password).
                        if crypt.crypt(pw, salt) == hashish:
                            print(pw)
                            return None


crack()