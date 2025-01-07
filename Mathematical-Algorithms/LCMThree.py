def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)

# recursive implementation
def LcmOfArray(arr, idx):

    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/__gcd(a,b)) # __gcd(a,b) is inbuilt library function

arr = [1,2,8,3]
print(LcmOfArray(arr, 0))
arr = [2,7,3,9,4]
print(LcmOfArray(arr,0))

# This code is contributed by divyeshrabadiya07.