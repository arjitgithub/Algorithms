# Python3 code to compute k-th
# digit in a^b
def kthdigit(a, b, k):

    # computing a^b in python
    p = a ** b
    count = 0

    while (p > 0 and count < k):

        # getting last digit
        rem = p % 10

        # increasing count by 1
        count = count + 1

        # if current number is
        # required digit
        if (count == k):
            return rem

        # remove last digit
        p = p / 10;

# driver code
a = 5
b = 2
k = 1
ans = kthdigit(a, b, k)
print (ans)

# This code is contributed by Saloni Gupta
