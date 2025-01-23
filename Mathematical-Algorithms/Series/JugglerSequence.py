'''
Juggler Sequence is a series of integer number in which the first term starts with a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation :
a_{k+1}=\begin{Bmatrix} \lfloor a_{k}^{1/2} \rfloor & for \quad even \quad a_k\\ \lfloor a_{k}^{3/2} \rfloor & for \quad odd \quad a_k \end{Bmatrix}


Juggler Sequence starting with number 3:
3, 5, 11, 36, 6, 2, 1
Juggler Sequence starting with number 9:
9, 27, 140, 11, 36, 6, 2, 1
Given a number n we have to print the Juggler Sequence for this number as the first term of the sequence.


Examples:

Juggler Sequence starting with number 3:
3, 5, 11, 36, 6, 2, 1
Juggler Sequence starting with number 9:
9, 27, 140, 11, 36, 6, 2, 1
Given a number n we have to print the Juggler Sequence for this number as the first term of the sequence.

Examples:

Input: 9
Output: 9, 27, 140, 11, 36, 6, 2, 1
We start with 9 and use above formula to get
next terms.

Input: 6
Output: 6, 2, 1

'''

import math

#This function prints the juggler Sequence
def printJuggler(n) :
    a = n

    # print the first term
    print (a,end=" ")

    # calculate terms until last term is not 1
    while (a != 1) :
        b = 0

        # Check if previous term is even or odd
        if (a%2 == 0) :

            # calculate next term
            b = (int)(math.floor(math.sqrt(a)))

        else :
            # for odd previous term calculate
            # next term
            b = (int) (math.floor(math.sqrt(a)*math.sqrt(a)*
                                  math.sqrt(a)))

        print (b,end=" ")
        a = b

printJuggler(3)
print()
printJuggler(9)

# This code is contributed by Nikita Tiwari.

"""
// Java implementation of Juggler Sequence 
import java.io.*; 
import java.math.*; 

class GFG { 
	
	// This function prints the juggler Sequence 
	static void printJuggler(int n) 
	{ 
		int a = n; 
	
	// print the first term 
	System.out.print(a+" "); 
	
	// calculate terms until last term is not 1 
	while (a != 1) 
	{ 
		int b = 0; 
	
		// Check if previous term is even or odd 
		if (a%2 == 0) 
	
			// calculate next term 
				b = (int)Math.floor(Math.sqrt(a)); 
	
		else
	
			// for odd previous term calculate 
			// next term 
				b =(int) Math.floor(Math.sqrt(a) * 
							Math.sqrt(a) * Math.sqrt(a)); 
	
		System.out.print( b+" "); 
		a = b; 
		} 
	} 

// Driver program to test above function 
public static void main (String[] args) { 
	printJuggler(3); 
	System.out.println(); 
	printJuggler(9); 
	} 
} 

//This code is contributed by Nikita Tiwari. 

"""
'''
Output: 
 
3 5 11 36 6 2 1 
9 27 140 11 36 6 2 1

Time complexity: O(nlogn) since using a single while loop and finding square root takes logarithmic time.

Space complexity: O(1) for constant variables

Important Points: 

The terms in Juggler Sequence first increase to a peak value and then start decreasing.
The last term in Juggler Sequence is always 1.
'''