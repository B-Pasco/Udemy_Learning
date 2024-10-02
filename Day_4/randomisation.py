# importing random library of python
import random

# print random nbr btn 0 <= nbr < 1, 1 is not included.
# nbr_float = random.random()
# print(nbr_float)

# print random nbr btn a <= nbr <= b.
# nbr_float = random.randint(1,5)
# print(nbr_float)

# print random nbr btn a <= nbr <= b, it can return float nbr.
# nbr_float = random.uniform(1,5)
# print(nbr_float)

# we are going to build a randomisation game.

rand_h_or_t = random.randint(0,1)

if rand_h_or_t == 0:
    print("Heads")
else:
    print("Tails")

