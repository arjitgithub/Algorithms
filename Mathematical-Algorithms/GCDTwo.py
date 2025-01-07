# Python implementation of above approach
# iterative implementation
def getGCD(a, b):
    while(a > 0 and b > 0):
        if(a > b):
            a = a % b
        else:
            b = b % a

    if(a == 0):
        return b

    return a


def GcdOfArray(arr):
    gcd = 0
    for i in range(len(arr)):
        gcd = getGCD(gcd, arr[i])
    return gcd


# driver code to test above functions
arr = [1,2,3]
print(GcdOfArray(arr))

arr = [2,4,6,8]
print(GcdOfArray(arr))

# THIS CODE IS CONTRIBUTED BY YASH AGARWAL(YASHAGARWAL2852002)