# game called whose gonna pay the bill btn us?
# importing library
import random

friends = ['John', 'Alice', 'Bob', 'Pasco', 'Smith']

# options 1
rand_index = random.randint(0, 4)
print(friends[rand_index])

# options 2
print(random.choice(friends))

