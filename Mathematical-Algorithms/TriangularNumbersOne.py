# Python3 program to check if a number is a
# triangular number using quadratic equation.
import math

# Returns True if num is triangular
def isTriangular(num):

    if (num < 0):
        return False

    # Considering the equation n*(n+1)/2 = num
    # The equation is : a(n^2) + bn + c = 0
    c = (-2 * num)
    b, a = 1, 1
    d = (b * b) - (4 * a * c)

    if (d < 0):
        return False

    # Find roots of equation
    root1 = ( -b + math.sqrt(d)) / (2 * a)
    root2 = ( -b - math.sqrt(d)) / (2 * a)

    # checking if root1 is natural
    if (root1 > 0 and math.floor(root1) == root1):
        return True

    # checking if root2 is natural
    if (root2 > 0 and math.floor(root2) == root2):
        return True

    return False


# Driver code
n = 55
if (isTriangular(n)):
    print("The number is a triangular number")
else:
    print("The number is NOT a triangular number")

# This code is contributed by Smitha Dinesh Semwal