from math import sin
import matplotlib.pyplot as plt


def adc(value: float, bits: int, __range: tuple, __returned):
    """
    This function takes an input value and a value range and converts it to a position represented by n bits.
    :param value: The analog value we want to convert to digital.
    :param bits: The amount of bits we'll use to represent the digital output.
    :param __range: Tuple with the minimum and maximum values analog values we are to receive.
    :param __returned: Digital output.
    :return:
    """

    # Calculate the maximum weight we'll have to deal with. This is the distance between the minimum possible input and
    # the maximum one.
    width = __range[1] - __range[0]

    # Now, we divide that total width between the total amount of states we can make of the bits we have.
    # The bit height is the distance between two bit positions.
    bit_height = width/2**bits

    # This is the maximum integer bit positions we can put between the lowest part of the range and the current value.
    # Imagine we want to reach a certain height stacking up Lego pieces, without exceeding that height.
    # The amount of pieces we'd need would be the integer division between the given height (measured from the floor)
    # and the height of each Lego piece.
    position = int(((value - __range[0]) // bit_height))

    # Put it in the proper binary format.
    print("{0:0{width}b}".format(position, width=bits))

    # I think this is what should be returned,  a n bit binary value.
    __returned.append(position)

    # This, on the other hand, is a more visually representative one.
    return (value // bit_height)*bit_height


bit_amount = 3
returned = []

test = [-3+3*sin(i*6/100) for i in range(100)]
digital = [adc(test_i, bit_amount, (-6, 0), returned) for test_i in test]

plt.plot(test, label='Input values')
plt.plot(digital, label='Digital approximation')
plt.plot(returned, label='Returned bit position')
plt.legend()
plt.title('Analog Digital converter')
plt.show()


