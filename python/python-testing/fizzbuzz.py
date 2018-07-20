"""my implementation of fizzbuzz"""
def fizz_buzz(num):
    """Prints different words for certain natural numbers

    This function prints out fizz when a number is divisible by 3, buzz when
    divisible by 5, and fizzbuzz when divisible by both.

    Args:
        num: (int) The number to convert based on fizzbuzz rules.

    """
    
    if ((num%3 == 0) and (num%5 == 0)):
        print("fizzbuzz")
    elif num%3 == 0:
        print("fizz")
    elif num%5 == 0:
        print("buzz")
    else:
        print(num)


for this in range(1, 100):
    fizz_buzz(this)
