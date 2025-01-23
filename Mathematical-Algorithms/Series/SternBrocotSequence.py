'''
Stern Brocot sequence is similar to Fibonacci sequence but it is different in the way fibonacci sequence is generated .
Generation of Stern Brocot sequence :

1. First and second element of the sequence is 1 and 1.
2. Consider the second member of the sequence . Then, sum the considered member of the sequence and it’s precedent i.e (1 + 1 = 2) .
   Now 2 is the next element of our series . Sequence will be [ 1, 1, 2 ]
3. After this element, our next element of the sequence will be the considered element of our second step.
   Now the sequence will be [ 1, 1, 2, 1 ]
4. Again we do the step 2, but now the considered element will be 2(3rd element ).
   So, next number of sequence will be sum of considered number and it’s precedent (2 + 1 = 3).
   Sequence will be now [ 1, 1, 2, 1, 3 ]
5. Like step 3, the next element will be the considered element i.e 2 . Thus sequence will be [ 1, 1, 2, 1, 3, 2 ]
6. Hence this process continues, now next considered element will be 1( 4th element ) .

Here is the simple program to print Stern Brocot sequence .
'''

# Python program to print
# Brocot Sequence
import math

def SternSequenceFunc(BrocotSequence, n):

    # loop to create sequence
    for i in range(1, n):

        considered_element = BrocotSequence[i]
        precedent = BrocotSequence[i-1]

        # adding sum of considered
        # element and it's precedent
        BrocotSequence.append(considered_element + precedent)

        # adding next considered element
        BrocotSequence.append(considered_element)


    # printing sequence..
    for i in range(0, 15):
        print(BrocotSequence[i] , end=" ")

# Driver code
n = 15
BrocotSequence = []

# adding first two element
# in the sequence
BrocotSequence.append(1)
BrocotSequence.append(1)

SternSequenceFunc(BrocotSequence, n)

# This code is contributed by Gitanjali.

'''
// Java program to print 
// Brocot Sequence
import java.io.*;
import java.util.*;

class GFG {
	
static void SternSequenceFunc(Vector<Integer>
						BrocotSequence, int n)
{
	// loop to create sequence
	for (int i = 1; BrocotSequence.size() < n; i++)
	{
		int considered_element = BrocotSequence.get(i);
		int precedent = BrocotSequence.get(i-1);

		// adding sum of considered element and it's precedent
		BrocotSequence.add(considered_element + precedent);
		
		// adding next considered element
		BrocotSequence.add(considered_element);
	}

	// printing sequence..
	for (int i = 0; i < 15; ++i)
		System.out.print(BrocotSequence.get(i) + " ");
}
	// Driver code
	public static void main (String[] args) {
		
		int n = 15;
		Vector<Integer> BrocotSequence = new Vector<Integer>();
		
		// adding first two element
		// in the sequence
		BrocotSequence.add(1);
		BrocotSequence.add(1);
		
		SternSequenceFunc(BrocotSequence, n);
		
	}
}

// This code is contributed by Gitanjali.

Output: 
1 1 2 1 3 2 3 1 4 3 5 2 5 3 4

'''
