# Python Code to find the sum of digits by
# taking the input number as string

def sumOfDigits(s):
    sum = 0
    for i in range(len(s)):

        # Extract digit from character
        digit = ord(s[i]) - ord('0')

        # Add digit to the sum
        sum = sum + digit
    return sum

if __name__ == "__main__":
    s = "123456789123456789123422"
    print(sumOfDigits(s))