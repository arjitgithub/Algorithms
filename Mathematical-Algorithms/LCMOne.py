# Python program to find LCM of two numbers

# Function to return LCM of two numbers
def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

# Driver program to test above function
if __name__ == '__main__':
    a = 10
    b = 5
    print("LCM of", a, "and", b, "is", LCM(a, b))