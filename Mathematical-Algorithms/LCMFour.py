from functools import reduce
import math

def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)

numbers = [2, 3, 4, 5]
print("LCM of", numbers, "is", lcm(numbers))