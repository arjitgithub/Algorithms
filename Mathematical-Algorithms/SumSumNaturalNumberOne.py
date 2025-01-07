# Python 3 program to find sum
# series 1, 3, 6, 10, 15, 21...
# and then find its sum*/

# Function to find the sum of series
def seriesSum(n):

    return int((n * (n + 1) * (n + 2)) / 6)


# Driver code
n = 4
print(seriesSum(n))

# This code is contributed by Smitha.