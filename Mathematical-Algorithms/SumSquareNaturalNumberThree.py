# We recursively call for n – 1 and add n^2 to the result.

def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)
n=8
print(sum_of_squares(n))