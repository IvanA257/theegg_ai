class Solitaire:
    def __init__(self, seed=[i for i in range(1,55,1)]):
        self.seed = seed
        self.deck = self.seed

    def circular_insert(self, element, index):

        # Manage index out of range
        while index >= 54 and index < 0:
            if index >= 54:
                index = index - 54

            if index < 0:
                idex = index + 54

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
        self.deck.insert(index_A + 1, 53)

    def move_joker_B(self):
        """
        This function finds the index of the element '54', which will be considered the joker B. Step 2
        :return:
        """
        index_B = self.deck.index(54)
        del self.deck[index_B]
        self.deck.insert(index_B - 2, 54)

    def switch_out_of_jokers(self):
        """
        This function takes the cards after the second joker and switches them with the ones before, step 3
        :return:
        """
        index_A = self.deck.index(53)
        index_B = self.deck.index(54)

        pre_jokers = self.deck[0:index_A]
        mid = self.deck[index_A:index_B]
        post_jokers = self.deck[index_B:-1]

        self.deck = post_jokers + mid + pre_jokers

