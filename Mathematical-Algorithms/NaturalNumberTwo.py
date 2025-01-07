# Efficient Python program to find the sum
# of first n natural numbers that avoid
# overflow if the result is going to be
# within limits.

# Returns sum of first n natural
# numbers
def findSum(n):
    if (n % 2 == 0):
        return (n / 2) * (n + 1)

    # If n is odd, (n+1) must be even
    else:
        return ((n + 1) / 2) * n


# Driver code
n = 5
print(findSum(n))