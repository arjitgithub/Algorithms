# Python Code to find number of digits by converting number to
# string

def count_digit(n):

    # Convert number to string
    num = str(n)

    # Calculate the length of the string
    return len(num)

if __name__ == "__main__":
    n = 58964
    print( count_digit(n))