import string
"""
README: The Solitaire encoding algorithm was implemented using object oriented programming. The encoding and decoding
        methods are called encode and decode respectively. They are the last 2 declared methods. 
"""


class Solitaire:
    def __init__(self, seed=[i for i in range(1,55,1)]):
        self.seed = seed
        self.deck = self.seed.copy()
        self.coding_key = []

    def reset(self):
        self.deck = self.seed.copy()
        self.coding_key = []

    def circular_insert(self, element, index):

        # Manage index out of range
        while index >= 54 or index < 0:
            if index >= 54:
                index = index - 53

            if index < 0:
                index = index + 53

        self.deck.insert(index, element)

    def move_joker_A(self):
        """
        This function finds the index of the element '53', which will be considered the joker A. Step 1
        :return:
        """

        # Find the A joker
        index_A = self.deck.index(53)
        # Remove it
        del self.deck[index_A]
        # Now place it in the next position
        self.circular_insert(53, index_A + 1)

    def move_joker_B(self):
        """
        This function finds the index of the element '54', which will be considered the joker B. Step 2
        :return:
        """
        index_B = self.deck.index(54)
        del self.deck[index_B]
        self.circular_insert(54, index_B + 2)

    def stage_3(self):
        """
        This function takes the cards after the second joker and switches them with the ones before, step 3
        :return:
        """
        index_A = self.deck.index(53)
        index_B = self.deck.index(54)

        # Switch them if index_B is before index_A, this is done because the rest of the function implicitly assumes
        # index_A to be the first one.
        if index_A > index_B:
            tmp = index_A
            index_A = index_B
            index_B = tmp

        pre_jokers = self.deck[0:index_A]
        mid = self.deck[index_A:index_B+1]
        post_jokers = self.deck[index_B+1:]

        self.deck = post_jokers + mid + pre_jokers


    def stage_4(self):
        """
        This function implements the fourth stage of the sequence generation.
        :return:
        """

        # We take the number into the last card.
        last_index = self.deck[-1]  # Cause it begins to count with one instead of zero.

        first_deck = self.deck[0:last_index]
        second_deck = self.deck[last_index:-1]

        # Now we switch both decks without changing the last card.
        # If last card in deck is a joker, then do nothing.
        if last_index > 0 and last_index < 53:
            self.deck = second_deck + first_deck + [last_index]

    def get_letter(self):
        """
        This function implements the four stages described in the web and gets a new letter from the deck.
        :return:
        """

        # Run the four stages of the algorithm
        self.move_joker_A()
        self.move_joker_B()
        self.stage_3()
        self.stage_4()


        first_index = self.deck[0]

        tmp = -1
        if first_index < 53:
            tmp = self.deck[first_index]

        # If the picked card is in the upper part of the deck then, we subtract 26 to it, because we need a number
        # between 1 and 26.
            if tmp > 26:
                tmp -= 26

            # NOTE THAT we only append the picked card if it is smaller than 53. Thus, if it is no joker.
            self.coding_key.append(tmp)

        return tmp

    def get_sequence(self, length):
        """
        This function returns a coding/decoding sequence. I decided to use a while because I don't know how many times
        a joker card will be obtained (remenber that a joker card cannot be used for the coding/decoding process, one
        needs to repeat the process and get another card). Therefore, a while structure was my way to obtain a sequence
        of a certain length.
        :param length: The length of the coding/decoding sequence we want to obtain.
        :return: The coding/decoding sequence itself.
        """

        while (len(self.coding_key) < length):
            self.get_letter()

        return self.coding_key

    def encode(self, message):
        """
        This function encodes the message.
        :param message: Original message we want to encode.
        :param code_sequence: Number sequence to be used in the encoding.
        :return: String with the encoded message.
        """

        # First, we obtain a coding sequence of the appropriate length.
        code_sequence = self.get_sequence(len(message))

        # Then, we convert the message to integers, each letter gets a number depending on its position in the
        # alphabet.
        message_to_int = [string.ascii_lowercase.index(i) for i in message.lower()]

        # Now, we add up the numbers of the message with the ones of the coding sequence.
        added_message = [(message_to_int[i] + code_sequence[i]) % 26 for i in range(len(message))]

        # Finally, the coded message is converted back to letters.
        letters_encoded = [string.ascii_lowercase[i] for i in added_message]

        # Reset coding_key
        self.reset()

        return ''.join(letters_encoded)

    def decode(self, message):
        """
        This function gets a coded message and recovers its original content.
        :param message: Coded message.
        :return: Decoded message.
        """

        # First, we obtain a coding sequence of the appropriate length.
        code_sequence = self.get_sequence(len(message))

        # Then, we convert the message to integers, each letter gets a number depending on its position in the
        # alphabet.
        message_to_int = [string.ascii_lowercase.index(i) for i in message.lower()]

        # Now, we subtract the numbers of the message with the ones of the coding sequence to get the original message
        # back.
        subtracted_message = [(message_to_int[i] - code_sequence[i]) % 26 for i in range(len(message))]

        # Finally, the decoded message is converted back to letters.
        letters_decoded = [string.ascii_lowercase[i] for i in subtracted_message]

        # Reset coding_key
        self.reset()

        return ''.join(letters_decoded)



sol = Solitaire()


hola = sol.encode('donotusepc')
print(hola)
print(sol.decode(hola))


