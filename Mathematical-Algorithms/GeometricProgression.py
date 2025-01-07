# Nikunj Sonigara

def Nth_of_GP(a, r, N):
    NthTerm = a
    for i in range(1, N):
        NthTerm *= r
    return NthTerm

def main():
    # Starting number
    a = 2

    # Common ratio
    r = 3

    # Nth term to be found
    N = 5

    # Function call
    print(f"The {N}th term of the series is: {Nth_of_GP(a, r, N)}")

if __name__ == "__main__":
    main()