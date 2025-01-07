def checkPalindrome(n):
    s = str(n)
    length = len(s)

    for i in range(length // 2):
        # Compare characters from the start and end
        if s[i] != s[length - i - 1]:
            return False

    # If no mismatch is found, it's a palindrome
    return True


if __name__ == "__main__":
    n = 1356531
    if(checkPalindrome(n) == True):
        print("true")
    else:
        print("false")