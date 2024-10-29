# make summation of the number
numbers = [12,32,435,54,654,765,87,543,75,76,87,65,453,765,976,987,1200]

sum = 0

for nbr in numbers:
    sum += nbr

print(sum)

# looking for the greatest number in the list.

highest = 0 # initializing the highest number as zero.
for nbr in numbers:
    if nbr > highest:
        highest = nbr
print(highest)