# Python3 Program to find nth
# term of geometric progression
import math


def Nth_of_GP(a, r, N):

    # Using formula to find the Nth
    # term TN = a1 * r(N-1)
    return(a * (int)(math.pow(r, N - 1)))


# Driver code
if __name__ == "__main__":
    a = 2  # Starting number
    r = 3  # Common ratio
    N = 5  # N th term to be find

    # Function call
    print("The", N, "th term of the series is :",
          Nth_of_GP(a, r, N))


# This code is contributed by Smitha Dinesh Semwal