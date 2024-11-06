# Target is the number up to which we count
# The actual target was to debug this code of game.
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            number = "FizzBuzz"
            print(number)
        elif number % 3 == 0:
            number = "Fizz"
            print(number)
        elif number % 5 == 0:
            number = "Buzz"
            print(number)
        else:
            print(number)


fizz_buzz(20)