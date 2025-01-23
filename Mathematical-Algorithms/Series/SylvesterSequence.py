'''
In number system, Sylvester’s sequence is an integer sequence in which each member of the sequence is the product of the previous members, plus one.
Given a positive integer N. The task is to print the first N member of the sequence.
Since numbers can be very big, use %10^9 + 7.
Examples:


Input : N = 6
Output : 2 3 7 43 1807 3263443

Input : N = 2
Output : 2 3


The idea is to run a loop and take two variables and initialise them as 1 and 2,
one to store the product till now and other to store the current number
which is nothing but the first number + 1 and for each step multiply
both using arithmetic modular operation i.e (a + b)%N = (a%N + b%N)%N where N is a modular number.
Below is the implementation of this approach:

'''

# Python Code for Sylvester sequence

def printSequence(n) :
    a = 1 # To store the product.
    ans = 2 # To store the current number.
    N = 1000000007

    # Loop till n.
    i = 1
    while i <= n :
        print(ans),
        ans = ((a % N) * (ans % N)) % N
        a = ans
        ans = (ans + 1) % N
        i = i + 1


# Driver program to test above function
n = 6
printSequence(n)

# This code is contributed by Nikita Tiwari.

'''
// JAVA Code for Sylvester sequence 
import java.util.*; 

class GFG { 
	
	public static void printSequence(int n) 
	{ 
		int a = 1; // To store the product. 
		int ans = 2; // To store the current number. 
		int N = 1000000007; 
		
		// Loop till n. 
		for (int i = 1; i <= n; i++) { 
		System.out.print(ans + " "); 
			ans = ((a % N) * (ans % N)) % N; 
			a = ans; 
			ans = (ans + 1) % N; 
		} 
	} 

	/* Driver program to test above function */
	public static void main(String[] args) 
	{ 
		int n = 6; 
		printSequence(n); 
		
	} 
} 
	
// This code is contributed by Arnav Kr. Mandal. 

Output: 
 
2 3 7 43 1807 3263443
Time complexity : O(n) 
Auxiliary Space : O(1)
'''