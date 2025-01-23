'''
Newman-Conway Sequence is the one that generates the following integer sequence.
1 1 2 2 3 4 4 4 5 6 7 7…

In mathematical terms, the sequence P(n) of Newman-Conway numbers is defined by the recurrence relation

P(n) = P(P(n - 1)) + P(n - P(n - 1))
with seed values P(1) = 1 and P(2) = 1

Given a number n, print n-th number in Newman-Conway Sequence.

Examples:

Input : n = 2
Output : 1

Input : n = 10
Output : 6
Method 1 (Use Recursion) :

A simple approach is direct recursive implementation of above recurrence relation.
'''
# Recursive function to find the n-th
# element of sequence
def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1));

# Driver code
def main():
    n = 10
    print(sequence(n))

if __name__ == '__main__':
    main()

"""
// Java program to find nth
// element of Newman-Conway Sequence
import java.io.*;

class GFG {
	
	// Recursion to find 
	// n-th element
	static int sequence(int n)
	{
		if (n == 1 || n == 2)
			return 1;
		else
			return sequence(sequence(n - 1)) 
				+ sequence(n - sequence(n - 1));
	}
	
	// Driver Program
	public static void main(String args[])
	{
		int n = 10;
		System.out.println(sequence(n));
	}
}

/*This code is contributed by Nikita Tiwari.*/

Output : 6

Time complexity: O(n)
Auxiliary Space: O(n)

Method 2 (Use Dynamic Programming): 
We can avoid repeated work done in method 1 by storing the values in the sequence in an array. 

// JAVA Code for Newman-Conway Sequence
import java.util.*;

class GFG {
	
	// Function to find the n-th element
	static int sequence(int n)
	{
		// Declare array to store sequence
		int f[] = new int[n + 1];
		f[0] = 0;
		f[1] = 1;
		f[2] = 1;

		int i;
	
		for (i = 3; i <= n; i++) 
			f[i] = f[f[i - 1]] +
						f[i - f[i - 1]]; 
	
		return f[n];
	}
	
	/* Driver program to test above function */
	public static void main(String[] args) 
	{
		int n = 10;
		System.out.println(sequence(n));

	}
}

// This code is contributed by Arnav Kr. Mandal.

"""

''' Python program to find the n-th element of 
	Newman-Conway Sequence'''

# To declare array import module array
import array
def sequence(n):
    f = array.array('i', [0, 1, 1])

    # To store values of sequence in array
    for i in range(3, n + 1):
        r = f[f[i-1]]+f[i-f[i-1]]
        f.append(r);

    return r

# Driver code
def main():
    n = 10
    print(sequence(n))

if __name__ == '__main__':
    main()

'''
Output : 6

Time complexity: O(n) 
Auxiliary Space: O(n) 
'''
