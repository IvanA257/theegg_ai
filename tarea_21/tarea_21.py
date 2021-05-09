from math import floor, prod


def get_factorized(num):
    """
    This function factorizes of the input number and returns all of them as an array.
    :param num: Input integer.
    :return result : Array with every factor of the input number.
    """

    # As we're only accepting integers we'll raise an exception if the input is not a positive one.
    if not isinstance(num, int) and num <= 0:
        raise TypeError("Only positive integers are allowed")

    result = [1]

    # The most basic way of finding factors is to iterate through all of the previous integers and check every of them.
    # Once we find a divisor, we'll divide our number with it and break the loop to re-start looking for divisors from 2
    while num > 1:
        for i in range(2, int(num) + 1):
            if num % i == 0:
                result.append(i)
                num /= i
                break
    return result

def get_irreductible_fraction(num):
    """
    The purpose of this function is to calculate the irreducible fraction for the given input number.
    :param num: Input decimal number, it has to be between 0.0001 and 0.9999. Maximum precission of 4 digits.
    :return result : String with the irreducible fraction of the input number.
    """

    # To ensure that decimal numbers ahead of the fourth will not be taken, we'll move the decimal point 4 places to the
    # right and then neglect the rest of the numbers.
    numerator = floor(num * 10000)
    denominator = 10000

    # The above proces converts our input number, e.g. 0.9999 into 9999/10000.

    # Now we get both numerator and denominator factorized.
    num_divisors = get_factorized(numerator)
    tmp_num_divisors = num_divisors.copy() # This prevents issues when iterating and removing items at the same time.
    denom_divisors = get_factorized(denominator)

    # Now we iterate over the lists of factors and remove every common one.
    for divisor in tmp_num_divisors:
        if divisor in denom_divisors:
            num_divisors.remove(divisor)
            denom_divisors.remove(divisor)

    irreducible_num = prod(num_divisors)
    irreducible_denim = prod(denom_divisors)

    result = "The irreducible fraction for the input number {} is {}/{}".format(num, irreducible_num, irreducible_denim)

    return result

print(get_irreductible_fraction(0.60))

#print(get_factorized(15))

