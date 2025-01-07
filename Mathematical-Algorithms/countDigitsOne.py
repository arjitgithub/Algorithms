# Recursive Python program to count
# number of digits in a number

def countDigit(n):
    if n//10 == 0:
        return 1
    return 1 + countDigit(n // 10)

if __name__ == "__main__":
    n = 58964
    print(countDigit(n))