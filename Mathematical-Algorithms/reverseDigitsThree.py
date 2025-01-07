# Python 3 program to reverse a number
def reversDigits(n):

    # converting number to string
    s = str(n)

    # reversing the string
    s = list(s)
    s.reverse()
    s = ''.join(s)

    # converting string to integer
    n = int(s)
    return n

if __name__ == "__main__":

    num = 4562
    print(reversDigits(num))