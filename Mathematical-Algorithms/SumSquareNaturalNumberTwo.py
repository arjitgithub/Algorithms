# Python program to get the sum
# of the following series

# Function calculating
# the series
def summation(n):
    return (n * (n + 1) // 2) * (2 * n + 1) // 3

# Driver Code
def main():
    n = 10
    print(summation(n))

if __name__ == "__main__":
    main()

# This code is contributed by shubhamsingh