# Python 3 program to find
# factorial of given number
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


# Driver Code
num = 5
print(f"Factorial of {num} is {factorial(num)}")