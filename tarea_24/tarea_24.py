from math import sin
import matplotlib.pyplot as plt


def adc(value, bits, range, returned):

    # Calculate the maximum weight we'll have to deal with. This is the distance between the minimum possible input and
    # the maximum one.
    width = range[1] - range[0]
    print('width: ', width)

    # Now, we divide that total weight between the total amount of states we can make of the bits we have.
    bit_height = width/2**bits
    print('bit_height: ', bit_height)

    # This is the outcoeme I think should be given
    returned.append((value // bit_height) + 2**(bits-1))

    # This, on the other hand, is a more visually representative one.
    return (value // bit_height)*bit_height

bit_amount = 3
returned = []

test = [sin(i*6/100) for i in range(100)]
digital = [adc(test_i, bit_amount, (-1, 1), returned) for test_i in test]

plt.plot(test)
plt.plot(digital)
plt.plot(returned)
plt.show()


