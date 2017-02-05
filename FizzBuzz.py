# Program prints numbers from 1 to 100
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by both 3 and 5, print "FizzBuzz"
# Created by JJ Marrs 


def fizzbuzz():
    numbers = list(range(1, 101))
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
