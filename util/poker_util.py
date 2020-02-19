import copy
from collections import Counter
from itertools import combinations

class poker_util:
  def create_card(self, nums, suits):
    """

    :param nums: list of integers 1-13
    :param suits: list of strings
    :return: List of Tuples for deck of 52 cards
    """
    final = []
    for s in suits:
      for n in nums:
        final.append((n, s))
    return final

  def card_count(self, board):  # count of each numbers in the board
    """function for counting cards, needed for pairs, 3 kinds, 4 of a kind
    input: board - a list of tuples for cards in hand
    output: counts - dict subclass of counts for each number in the hand cards
    """
    nums = []
    for v in board:
      nums.append(v[0])  # index 0 contains onnly the numbers so ignoring the suit for num count
    counts = Counter(nums)
    return counts

  def suite_count(self, board):  # count of each suit in the board
    """function for counting cards of same suit
    input: board - a list of tuples for cards in hand
    output: counts - dict subclass of counts for each suit in the hand cards
    """
    ss = []
    for v in board:
      ss.append(v[1])  # index 1 contains the suit so ignoring the num for suit count
    counts = Counter(ss)
    return counts

  def calculate_max_streak(self, board):  # is continuous function return max streak
    """function for getting maximum number of contiguos cards
    input: board - a list of tuples for cards in hand
    output: max_streak - integer variable for highest value of contigous numbers in the hand
    """
    nums = []
    for v in board:
      nums.append(v[0])
    nums = sorted(nums)
    nums = list(set(nums))
    max_streak = 1
    streak = 1
    for i in range(len(nums) - 1):
      if nums[i + 1] == nums[i] + 1:
        streak = streak + 1
        if streak > max_streak:
          max_streak = streak
      else:
        streak = 1
    if nums[0] == 1 and nums[
      -1] == 13:  # this condition deals with the special case where Ace forms a streak with kings rather than 2.
      nums.pop(0)  # removing 1
      nums.append(14)  # adding 14 for our Ace
      # count process is done again as hand plus board cards may have different number of total cards in different formats of poker. and is continuous function does not limit itself to a streak of 5.
      # so to have all cases included, re-run the loop for this special case.
      for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
          streak = streak + 1
          if streak > max_streak:
            max_streak = streak
        else:
          streak = 1
    return max_streak

  def calculate_hand(self, board):
    """this function tells you what is the highest hand with a hand of cards
    input: board - a list of tuples for cards in hand
    output: highest_hand - a string showing the highest rank the cards in hand has.
    """
    n_counts = self.card_count(board)
    ss_counts = self.suite_count(board)
    num_straight = self.calculate_max_streak(board)
    highest_freq = n_counts.most_common(1)[0][1]
    second_highest_freq = n_counts.most_common(2)[1][1]
    ss_count_max = ss_counts.most_common(1)[0][1]
    ss_suit = ss_counts.most_common(1)[0][0]
    highest_hand = "high card"
    if num_straight >= 5 and ss_count_max >= 5:
      nums = []
      for v in board:
        if v[1] == ss_suit:
          nums.append(v[0])
      nums = sorted(nums)
      nums = list(set(nums))
      if nums[0] == 1 and nums[-4:] == [10, 11, 12, 13]:
        highest_hand = "roy flush"
      else:
        max_streak = 1
        streak = 1
        for i in range(len(nums) - 1):
          if nums[i + 1] == nums[i] + 1:
            streak = streak + 1
            if streak > max_streak:
              max_streak = streak
          else:
            streak = 1
        if max_streak >= 5:
          highest_hand = "str flush"
    elif highest_freq == 4:
      highest_hand = "4 kind"
    elif highest_freq == 3 and second_highest_freq == 2:
      highest_hand = "full house"
    elif ss_count_max >= 5:
      highest_hand = "flush"
    elif num_straight >= 5:
      highest_hand = "str"
    elif highest_freq == 3:
      highest_hand = "3 kind"
    elif highest_freq == 2 and second_highest_freq == 2:
      highest_hand = "2 pair"
    elif highest_freq == 2 and second_highest_freq < 2:
      highest_hand = "pair"
    return highest_hand

  def calculate_possibility(self, board, my_hand, hands_num, cards):
    """The possibility function. The format defined is of Texas Holdem Poker. With a board of cards opened up, what is the highest rank of combination out there
    input: board - a list of tuples for cards in hand
           cards - list of tuples of all the cards in the deck

    output: highest - int value of the highest possibility of hand that can be achieved when all the board cards are opened.
    """
    r = 7 - len(board)
    temp = copy.deepcopy(cards)
    for b in board + my_hand:
      temp.remove(b)
    l = [list(x) for x in combinations(temp, r)]
    highest = 1
    for option in l:
      final = board + option
      temp = self.calculate_hand(final)
      if hands_num[temp] > highest:
        highest = hands_num[temp]
        maximum = copy.deepcopy(final)
        # print(final)
      final = final[:len(board)]
    print("Opposition's highest hand+board can be:", maximum)
    return highest