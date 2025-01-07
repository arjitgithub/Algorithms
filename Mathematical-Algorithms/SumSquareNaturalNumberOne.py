# Python3 program to
# calculate 1 ^ 2 + 2 ^ 2 + 3 ^ 2+..
# A naive approach will be to run a loop from 1 to n and sum up all the squares. 

# Python code to find sum of
# squares of first n natural numbers.
def summation(n):
    return (n * (n + 1) *
            (2 * n + 1)) / 6

# Driver Code
if __name__ == '__main__':
    n = 10
    print(summation(n))