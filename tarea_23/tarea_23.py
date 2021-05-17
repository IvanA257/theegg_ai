class Solitaire:
    def __init__(self, seed=[i for i in range(1,55,1)]):
        self.seed = seed
        self.deck = self.seed
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
        # print('first deck: ', first_deck)
        second_deck = self.deck[last_index:-1]
        # print('second deck: ', second_deck)

        # Now we switch both decks without changing the last card.
        # If last card in deck is a joker, then do nothing.
        if last_index > 0 and last_index < 53:
            self.deck = second_deck + first_deck + [last_index]

    def get_letter(self):
        """
        This function implements the four stages and gets a new letter from the deck.
        :return:
        """

        # Run the four stages of the algorithm
        self.move_joker_A()
        print(self.deck)
        self.move_joker_B()
        print(self.deck)
        self.stage_3()
        print(self.deck)
        self.stage_4()
        print(self.deck, '\n--------------------------------------------------------------------')


        first_index = self.deck[0]

        tmp = self.deck[first_index]

        # If the picked card is in the upper part of the deck then, we subtract 26 to it, because we need a number
        # between 1 and 26.
        # if tmp > 26:
        #     tmp -= 26
        #     self.coding_key.append(tmp)
        #
        # else:
        self.coding_key.append(tmp)

        return tmp

sol = Solitaire()
# print(sol.deck)
# sol.move_joker_A()
# print(sol.deck)
# sol.move_joker_B()
# print(sol.deck)
# sol.stage_3()
# print(sol.deck)
# sol.stage_4()
# print(sol.deck)

for i in range(10):
    print(sol.get_letter())

print(sol.coding_key)