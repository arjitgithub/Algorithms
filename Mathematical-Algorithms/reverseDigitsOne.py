# Python 3 program to reverse digits
# of a number

def reverseDigits(n):
    revNum = 0
    basePos = 1
    if(n > 0):
        reverseDigits((int)(n / 10))
        revNum += (n % 10) * basePos
        basePos *= 10
    return revNum

if __name__ == "__main__":
    n = 4562
    print(reverseDigits(n))