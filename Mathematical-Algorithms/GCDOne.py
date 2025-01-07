# To find GCD of an array by recursive approach
import math

# Recursive Implementation
def GcdOfArray(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]

    a = arr[idx]
    b = GcdOfArray(arr,idx+1)

    return math.gcd(a, b)

# Driver Code
arr = [1, 2, 3]
print(GcdOfArray(arr,0))

arr = [2, 4, 6, 8]
print(GcdOfArray(arr,0))

# Code contributed by Gautam goel (gautamgoel962)