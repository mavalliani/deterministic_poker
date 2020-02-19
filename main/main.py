from util.poker_util import *

class Solution:
    cards = create_card(range(1, 14), ["h", "c", "d",
                                       "s"])  # creates tuples of cards 1 to 13 of the 4 suits (hearts, clubs, diamonds, spades). Aces is encoded as 1

    hands_num = {"high card": 1, "pair": 2, "2 pair": 3, "3 kind": 4, "str": 5, "flush": 6, "full house": 7,
                 "4 kind": 8, "str flush": 9, "roy flush": 10}
    num_hand = {1: "high card", 2: "pair", 3: "2 pair", 4: "3 kind", 5: "str", 6: "flush", 7: "full house",
                8: "4 kind",
                9: "str flush", 10: "roy flush"}

    def solve_hand(self, my_hand, board):
        """This is the main function. It shows:
        1. What is your highest hand.
        2. The highest rank of combination that the opponent may have with a certain board cards.

        To play deterministically, bet only if your hand is higher than the highest possibility of cards of the opponent. Else, Check/Fold.

        input:  my_hand - a list of tuples for cards in hand
                board - a list of tuples for cards in board

        output: prints my Current highest rank
                oppositions Possible higher ranks than my current

        """

        mine = calculate_hand(my_hand + board)

        opposite = calculate_possibility(board, my_hand, self.hands_num, self.cards)
        if self.hands_num[mine] > opposite:
            return ("Bet. Your hand is the highest:", mine)
        elif self.hands_num[mine] == opposite:
            return ("Bet cautiously. oppositions highest hand possibility is also:", self.num_hand[opposite])
        else:
            return ("Check/Fold. opposite highest hand possibility is:", self.num_hand[opposite])

    def execute_test_hand(self):
        input = [(3, 'h'), (4, 'h')], [(2, 's'), (3, 's'), (4, 's')]
        print("For given input of my hand {} and boards cards {} User should {}".format(input[0], input[1],
                                                                                        self.solve_hand(input[0], input[1])))

        input = [(3, 'h'), (4, 'h')], [(5, 'h'), (6, 'h'), (7, 'h')]
        print("For given input of my hand {} and boards cards {} User should {}".format(input[0], input[1],
                                                                                        self.solve_hand(input[0], input[1])))

        input = [(8, 'h'), (9, 'h')], [(5, 'h'), (6, 'h'), (7, 'h'), (2, "s"), (4, "d")]
        print("For given input of my hand {} and boards cards {} User should {}".format(input[0], input[1],
                                                                                        self.solve_hand(input[0], input[1])))

        input = [(13, 'h'), (13, 'd')], [(13, 's'), (13, 'c'), (11, 'h'), (10, "s"), (9, "d")]
        print("For given input of my hand {} and boards cards {} User should {}".format(input[0], input[1],
                                                                                        self.solve_hand(input[0], input[1])))
if __name__ == '__main__':
    solution = Solution()
    solution.execute_test_hand()

