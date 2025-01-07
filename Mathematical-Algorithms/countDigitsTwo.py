# Log based Python program to count number of
# digits in a number
import math

def countDigit(n):
    return math.floor(math.log10(n)+1)

if __name__ == "__main__":
    n = 58964
    print(countDigit(n))