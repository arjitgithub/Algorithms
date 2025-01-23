'''
Given an integer ‘n’, print the first ‘n’ terms of the Moser-de Bruijn Sequence.
Moser-de Bruijn sequence is the sequence obtained by adding up the distinct powers of the number 4 (For example, 1, 4, 16, 64, etc).

Examples:

Input : 5
Output : 0 1 4 5 16

Input : 10
Output : 0 1 4 5 16 17 20 21 64 65
It is observed that the terms of the sequence follow the recurrence relation :

1) S(2 * n) = 4 * S(n)
2) S(2 * n + 1) = 4 * S(n) + 1
with S(0) = 0 and S(1) = 1

It may be noted here that any number which is the sum of non-distinct powers of 4 is not a part of the sequence.

For example, 8 is not a part of the sequence because it is formed as the sum of non-distinct powers of 4, which are 4 and 4.
Thus, any number which is not a power of 4 and is present in the sequence must be the sum of the distinct powers of 4.

For example, 21 is a part of the sequence, even though it is not a power of 4,
because it is the sum of the distinct powers of 4, which are 1, 4, and 16.

Employ the recurrence relation discussed above to generate the sequence efficiently.
'''

# Python code to generate first
# 'n' terms of the Moser-de
# Bruijn Sequence

# Function to generate nth term
# of Moser-de Bruijn Sequence
def gen(n):

    # S(0) = 0
    if n == 0:
        return 0

    # S(1) = 1
    elif n ==1:
        return 1

    # S(2 * n) = 4 * S(n)
    elif n % 2 ==0:
        return 4 * gen(n // 2)

    # S(2 * n + 1) = 4 * S(n) + 1
    elif n % 2 == 1:
        return 4 * gen(n // 2) +1

# Generating the first 'n' terms
# of Moser-de Bruijn Sequence
def moserDeBruijn(n):
    for i in range(n):
        print(gen(i), end = " ")

# Driver Program
n = 15
print("First", n, "terms of ",
      "Moser-de Bruijn Sequence:")
moserDeBruijn(n)

# This code is contributed by Shrikant13

'''
// Java code to generate first 'n' terms 
// of the Moser-de Bruijn Sequence

class GFG 
{
	
// Function to generate nth term 
// of Moser-de Bruijn Sequence
public static int gen(int n)
{ 
	
	// S(0) = 0
	if (n == 0)
		return 0;
	
	// S(1) = 1
	else if (n == 1)
		return 1;
	
	// S(2 * n) = 4 * S(n)
	else if (n % 2 == 0)
		return 4 * gen(n / 2);
	
	// S(2 * n + 1) = 4 * S(n) + 1
	else if (n % 2 == 1)
		return 4 * gen(n / 2) + 1;
	return 0;
}

// Generating the first 'n' terms 
// of Moser-de Bruijn Sequence
public static void moserDeBruijn(int n)
{
	for (int i = 0; i < n; i++)
		System.out.print(gen(i) + " ");
	System.out.println();
}

// Driver Code
public static void main(String args[])
{
	int n = 15;
	System.out.println("First " + n + 
					" terms of " + 
	"Moser-de Bruijn Sequence : ");
	moserDeBruijn(n);
}
}

// This code is contributed by JaideepPyne.

'''
"""
Output : 

First 15 terms of Moser-de Bruijn Sequence : 
0 1 4 5 16 17 20 21 64 65 68 69 80 81 84

Time complexity: O(log2n)
Auxiliary Space: O(1)

// Java code to generate first 'n' terms 
// of the Moser-de Bruijn Sequence

class GFG 
{
	
// Function to generate nth term 
// of Moser-de Bruijn Sequence
static int gen(int n)
{ 
	int []S = new int [n + 1];

	S[0] = 0;
	if(n != 0)
		S[1] = 1;

	for (int i = 2; i <= n; i++)
	{ 
		
		// S(2 * n) = 4 * S(n)
		if (i % 2 == 0)
		S[i] = 4 * S[i / 2];
	
		// S(2 * n + 1) = 4 * S(n) + 1
		else
		S[i] = 4 * S[i/2] + 1;
	}
	
	return S[n];
}

// Generating the first 'n' terms 
// of Moser-de Bruijn Sequence
static void moserDeBruijn(int n)
{
	for (int i = 0; i < n; i++)
		System.out.print(gen(i)+" ");
}

// Driver Code
public static void main(String[] args)
{
	int n = 15;
	System.out.println("First " + n + 
					" terms of " + 
	"Moser-de Bruijn Sequence : ");
	moserDeBruijn(n);
}
}

// This code is contributed by 
// Smitha Dinesh Semwal.


"""

# python3 code to generate first 'n' terms
# of the Moser-de Bruijn Sequence

# Function to generate nth term
# of Moser-de Bruijn Sequence
def gen( n ):
    S = [0, 1]
    for i in range(2, n+1):

        # S(2 * n) = 4 * S(n)
        if i % 2 == 0:
            S.append(4 * S[int(i / 2)]);

        # S(2 * n + 1) = 4 * S(n) + 1
        else:
            S.append(4 * S[int(i / 2)] + 1);
    z = S[n];
    return z;

# Generating the first 'n' terms
# of Moser-de Bruijn Sequence
def moserDeBruijn(n):
    for i in range(n):
        print(gen(i), end = " ")

# Driver Code
n = 15
print("First", n, "terms of ",
      "Moser-de Brujn Sequence:")
moserDeBruijn(n)

# This code is contributed by mits.

'''
Output : 

First 15 terms of Moser-de Bruijn Sequence : 
0 1 4 5 16 17 20 21 64 65 68 69 80 81 84

Time complexity: O(n) since using a for loop
Auxiliary Space: O(n) for array 
'''

