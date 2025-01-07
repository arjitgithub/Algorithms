# Python 3 code
a = 2

d = 1
n = 5

nthTerm = a
for i in range(1, n):
    nthTerm += d
print(f'The {n}th term of the series is: {nthTerm}')