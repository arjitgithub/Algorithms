'''
Padovan Sequence similar to Fibonacci sequence with similar recursive structure. The recursive formula is,
  P(n) = P(n-2) + P(n-3)
  P(0) = P(1) = P(2) = 1

Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55……
Spiral of squares with side lengths which follow the Fibonacci sequence.

Padovan Sequence: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37,…..
Spiral of equilateral triangles with side lengths which follow the Padovan sequence.

Examples:


For Padovan Sequence:
P0 = P1 = P2 = 1 ,
P(7) = P(5) + P(4)
     = P(3) + P(2) + P(2) + P(1)
     = P(2) + P(1) + 1 + 1 + 1
     = 1 + 1 + 1 + 1 + 1
     = 5

'''

# Python program to find n'th term in Padovan
# Sequence using Dynamic Programming

# Function to calculate padovan number P(n)
def pad(n):

    # 0th ,1st and 2nd number of the series are 1
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1

    # Find n'th Padovan number using recursive
    # formula.
    for i in range(3, n+1):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext

    return pNext

# Driver Code
print (pad(12))

"""
// Java program to find n'th term
// in Padovan Sequence using
// Dynamic Programming
import java.io.*;

class GFG {
	
	/* Function to calculate
	padovan number P(n) */
	static int pad(int n)
	{
	int []padv=new int[n]; //create array to store padovan values
	padv[0]=padv[1]=padv[2]=1;
		for (int i = 3; i <= n; i++) {
		padv[i]=padv[i-2]+padv[i-3]; 
		}
		return padv[n-1];

		
	}

	/* Driver Program */
	public static void main(String args[])
	{
		int n = 12;
		System.out.println(pad(n));
	}
}

/*This code is contributed by Kanjam Bhat Lidhoo.*/

"""

'''
Output: 21
'''