# Python 3 program to reverse a number
def reversDigits(n):

    # converting number to string
    s = str(n)

    # reversing the string
    s = s[::-1]

    # converting string to integer
    n = int(s)

    # returning integer
    return n

if __name__ == "__main__":

    n = 4562
    print(reversDigits(n))