# Iterative Python program to count
# number of digits in a number

def countDigit(n):

    # Base case
    if n == 0:
        return 1

    count = 0

    # Iterate till n has digits remaining
    while n != 0:

        # Remove rightmost digit
        n = n // 10

        # Increment digit count by 1
        count += 1

    return count

if __name__ == "__main__":
    n = 58964
    print(countDigit(n))