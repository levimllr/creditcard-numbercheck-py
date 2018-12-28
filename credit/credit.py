import cs50
import math


# Credit will take a credit card number inputted by the user and determine if it is valid by applying Luhn's algorithm and checking proprietary constraints.
def credit():

    # Here we prompt the user for input.
    # The while loop will only accept values that are greater than 10^12 and less than 10^16, which roughly covers the range of CC#s.

    ccn = cs50.get_float("Credit Card Number: ")

    # Now we determine right off the bat if the CC# is valid by checking how long it is!
    # CC#s with a number of digits other than 13, 15, and 16 are invalid.

    count = 0
    n = ccn

    while n > 0:
        n = n//10
        count += 1

    if count != 13 and count != 15 and count != 16:
        print("INVALID")
        return None

    # Now it's time to apply Luhn's algorithm.
    # 1. We will multiply every other digit by 2, starting with the CC#'s second to last digit.
    # 2. We will add these doubled digits together.
    # 3. We will then add that sum to the sum of the digits not multiplied by 2.
    # 4. If the total modulo 10 (if the total's last digit) is 0, the number is VALID!!!

    # We will employ this algorithm using a FOR loop.
    # luhn1 will become the sum from steps 1 and 2.
    # luhn2 will become the sum from step 3.
    # lunn3 will become the total sum.

    luhn1 = 0
    luhn2 = 0
    luhn3 = 0

    # fmod allows use to apply the modulus operator the long long data type (numbers up to 64 bits in size).
    # The modulus gives us the remainder of a quotient. By dividing the modulus of a digit by the power of ten to the h just behind it (h-1), we can extract the digit of each tens place.
    # floor rounds a quotient down to the nearest whole number. We need this function to correct for computational imprecision.
    # We have an if/else statement to distinguish between numbers that, when doubled, are two digits.
    # Luhn's algorithm dictates that we add the doubled numbers' digits, not the double numbers themslves.
    # The if statement extracts the digits of a two-digit doubled number and adds them to luhn1.
    # The else statement adds single-digit doubled numbers to luhn1.
    for i in range(2, count + 1, 2):
        if ccn % 10**i >= 5:
            luhn1 += ((math.floor((ccn % (10**i)) // (10**(i - 1))) * 2) % 100) // 10 + ((math.floor((ccn % (10**i)) // (10**(i - 1))) * 2) % 10) // 1
        else:
            luhn1 += math.floor((ccn % (10**i)) // (10**(i - 1))) * 2

    # Any time you get a seemingly random print() commented out, know that is placed for debugging!
    # print(luhn1)

    # This next for loop adds the undoubled digits together.
    for j in range(1, count + 1, 2):
        luhn2 += math.floor((ccn % 10**j) // (10**(j-1)))

    # print(luhn2)

    # Now we create the total!
    luhn3 = luhn1 + luhn2

    # print(luhn3)

    # We need to extract the first two digits of our CC# to determine what type it is.
    first2 = math.floor(ccn // (10**(count - 2)))
    # print(first2)

    # The following if/elif/elif/else statements print the type of CC# entered.
    # Because VISA's designation is that the greatest tens digit be 4, we simply check to see that the two greatest digits are less than 50 or greater than or equal to 40.
    if luhn3 % 10 == 0 and (first2 == 37 or first2 == 34):
        print("AMEX")
    elif luhn3 % 10 == 0 and first2 >= 40 and first2 < 50:
        print("VISA")
    elif luhn3 % 10 == 0 and (first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55):
        print("MASTERCARD")
    else:
        print("INVALID")


# Now that we're in Python, we can't forget to execute the darn function ;)
credit()