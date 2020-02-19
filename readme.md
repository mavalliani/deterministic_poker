Playing Poker Determinstically
====================

### Introduction

A fun/playful method to beat someone in poker is thorugh patience and math. Except the intial calls to enter the round, deny all calls/raises. bet only when the code tells you to. This piece of code gives you:
1.	What is your highest hand.
2.	The highest rank of combination that the opponent may have with a certain board cards. To play deterministically, bet only if your hand is higher than the highest possibility of cards of the opponent. Else, Check/Fold.



### Further Work

Some future work can involve some probabilistic modeling around the coins lost making initial calls to enter the round and potential gains when the system tells you to bet. Then finding expectation will be awesome.


### Requirements

Python version 3.8 has been used for the work.

            
### Output of test cases in the program

Opposition's highest hand+board can be: [(2, 's'), (3, 's'), (4, 's'), (1, 'h'), (2, 'h'), (1, 's'), (5, 's')]
For given input of my hand [(3, 'h'), (4, 'h')] and boards cards [(2, 's'), (3, 's'), (4, 's')] User should ('Check/Fold. opposite highest hand possibility is:', 'str flush')

Opposition's highest hand+board can be: [(5, 'h'), (6, 'h'), (7, 'h'), (1, 'h'), (2, 'h'), (8, 'h'), (9, 'h')]
For given input of my hand [(3, 'h'), (4, 'h')] and boards cards [(5, 'h'), (6, 'h'), (7, 'h')] User should ('Bet cautiously. oppositions highest hand possibility is also:', 'str flush')

Opposition's highest hand+board can be: [(5, 'h'), (6, 'h'), (7, 'h'), (2, 's'), (4, 'd'), (3, 'h'), (4, 'h')]
For given input of my hand [(8, 'h'), (9, 'h')] and boards cards [(5, 'h'), (6, 'h'), (7, 'h'), (2, 's'), (4, 'd')] User should ('Bet cautiously. oppositions highest hand possibility is also:', 'str flush')

Opposition's highest hand+board can be: [(13, 's'), (13, 'c'), (11, 'h'), (10, 's'), (9, 'd'), (9, 'h'), (9, 'c')]
For given input of my hand [(13, 'h'), (13, 'd')] and boards cards [(13, 's'), (13, 'c'), (11, 'h'), (10, 's'), (9, 'd')] User should ('Bet. Your hand is the highest:', '4 kind')




----------------------------------