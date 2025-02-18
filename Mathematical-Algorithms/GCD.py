# GCD of more than two (or array) numbers

# Function implements the Euclidean
# algorithm to find H.C.F. of two number
def find_gcd(x, y):

    while(y):
        x, y = y, x % y

    return x

# Driver Code
l = [2, 4, 6, 8, 16]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)

# Code contributed by Mohit Gupta_OMG