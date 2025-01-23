'''
Given an integer n. Print first n elements of Recaman’s sequence.
Examples:


Input : n = 6
Output : 0, 1, 3, 6, 2, 7

Input  : n = 17
Output : 0, 1, 3, 6, 2, 7, 13, 20, 12, 21,
         11, 22, 10, 23, 9, 24, 8
It is basically a function with domain and co-domain as natural numbers and 0. It is recursively defined as below:
Specifically, let a(n) denote the (n+1)-th term. (0 is already there).
The rule says:

a(0) = 0,
if n > 0 and the number is not
   already included in the sequence,
     a(n) = a(n - 1) - n
else
     a(n) = a(n-1) + n.


Below is a simple implementation where we store all n Recaman Sequence numbers in an array.
We compute the next number using the recursive formula mentioned above.
'''
# Python 3 program to print n-th
# number in Recaman's sequence

# Prints first n terms of Recaman
# sequence
def recaman(n):

    # Create an array to store terms
    arr = [0] * n

    # First term of the sequence
    # is always 0
    arr[0] = 0
    print(arr[0], end=", ")

    # Fill remaining terms using
    # recursive formula.
    for i in range(1, n):

        curr = arr[i-1] - i
        for j in range(0, i):

            # If arr[i-1] - i is
            # negative or already
            # exists.
            if ((arr[j] == curr) or curr < 0):
                curr = arr[i-1] + i
                break

        arr[i] = curr
        print(arr[i], end=", ")

# Driver code
n = 17

recaman(n)

# This code is contributed by Smitha.

'''
// Java program to print n-th number in Recaman's 
// sequence
import java.io.*;

class GFG {
	
	// Prints first n terms of Recaman sequence
	static void recaman(int n)
	{
		// Create an array to store terms
		int arr[] = new int[n];
	
		// First term of the sequence is always 0
		arr[0] = 0;
		System.out.print(arr[0]+" ,");
	
		// Fill remaining terms using recursive
		// formula.
		for (int i = 1; i < n; i++)
		{
			int curr = arr[i - 1] - i;
			int j;
			for (j = 0; j < i; j++)
			{
				// If arr[i-1] - i is negative or
				// already exists.
				if ((arr[j] == curr) || curr < 0)
				{
					curr = arr[i - 1] + i;
					break;
				}
			}
	
			arr[i] = curr;
			System.out.print(arr[i]+", ");
			
		}
	}
	
	// Driver code
	public static void main (String[] args) 
	{
		int n = 17;
		recaman(n);

	}
}

// This code is contributed by vt_m

Output:  0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 

Time Complexity : O(n2) 
Auxiliary Space : O(n), since n extra space has been added
Optimizations :   We can use hashing to store previously computed values and can make this 
program work in O(n) time. 

// Java program to print n-th number 
// in Recaman's sequence
import java.util.*;

class GFG
{

// Prints first n terms of Recaman sequence
static void recaman(int n)
{
	if (n <= 0)
	return;

	// Print first term and store it in a hash 
	System.out.printf("%d, ", 0);
	HashSet<Integer> s = new HashSet<Integer>();
	s.add(0);

	// Print remaining terms using 
	// recursive formula.
	int prev = 0;
	for (int i = 1; i< n; i++)
	{
		int curr = prev - i;

		// If arr[i-1] - i is negative or
		// already exists.
		if (curr < 0 || s.contains(curr))
			curr = prev + i;

		s.add(curr);

		System.out.printf("%d, ", curr);
		prev = curr;
	}
}

// Driver code
public static void main(String[] args)
{
	int n = 17;
	recaman(n);
}
}

// This code is contributed by Rajput-Ji


'''

# Python3 program to print n-th number in
# Recaman's sequence

# Prints first n terms of Recaman sequence
def recaman(n):

    if(n <= 0):
        return

    # Print first term and store it in a hash
    print(0, ",", end='')
    s = set([])
    s.add(0)

    # Print remaining terms using recursive
    # formula.
    prev = 0
    for i in range(1, n):

        curr = prev - i

        # If arr[i-1] - i is negative or
        # already exists.
        if(curr < 0 or curr in s):
            curr = prev + i

        s.add(curr)

        print(curr, ",", end='')
        prev = curr

# Driver code
if __name__=='__main__':
    n = 17
    recaman(n)

# This code is contributed by
# Sanjit_Prasad

'''
Output: 
0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 
Time Complexity : O(n) 
Auxiliary Space : O(n), since n extra space has been taken.
'''

