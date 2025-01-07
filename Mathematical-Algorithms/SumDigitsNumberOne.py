# Recursive Python Code to find sum of digits

def sumOfDigits(n):

    # Base Case
    if n == 0:
        return 0

    # Recursive Case
    return n % 10 + sumOfDigits(n // 10)


if __name__ == "__main__":
    print(sumOfDigits(12345))