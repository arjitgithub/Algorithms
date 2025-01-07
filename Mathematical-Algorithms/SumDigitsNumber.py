# Iterative Python Code to find sum of digits

def sumOfDigits(n):
    sum = 0
    while n != 0:

        # Extract the last digit
        last = n % 10

        # Add last digit to sum
        sum += last

        # Remove the last digit
        n //= 10
    return sum

if __name__ == "__main__":
    n = 12345
    print(sumOfDigits(n))