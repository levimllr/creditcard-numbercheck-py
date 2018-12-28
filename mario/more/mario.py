from cs50 import get_int


def pyramid():
    # Prompt user for a positive number equal to or less than 23.
    # We set n = -1 for starters in order to trigger the while loop!
    n = -1
    while n < 0 or n > 23:
        n = get_int("Positive number: ")
    # Now we print the resulting pyramid row by row (i by i).
    for i in range(n):
        for j in range(n - 1, i, -1):
            # We have to take care to set the ending of the print function to "" so that a new line is not started.
            print(" ", end="")
        for k in range(i + 1):
            print("#", end="")
        print("  ", end="")
        for l in range(i + 1):
            print("#", end="")
        print("")


# Finally, we run the pyramid function!
pyramid()