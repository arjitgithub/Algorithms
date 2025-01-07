# Python3 program to find sum
# series 1, 3, 6, 10, 15, 21...
# and then find its sum.

# Function to find the sum of series
def seriessum(n):

    sum = 0
    for i in range(1, n + 1):
        sum += i * (i + 1) / 2
    return sum

# Driver code
n = 4
print(seriessum(n))

# This code is Contributed by Azkia Anam.