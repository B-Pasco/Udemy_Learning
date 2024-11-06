import maths # This is module I have created
from random import randint

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += randint(1, 3)
        new_item = maths.add(new_item, item)
        # This line of code had indention error but runs.
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
