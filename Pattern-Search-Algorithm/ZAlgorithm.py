'''Z algorithm (Linear time pattern searching Algorithm)
Last Updated : 16 Jul, 2024
This algorithm efficiently locates all instances of a specific pattern within a text in linear time. If the length of the text is “n” and the length of the pattern is “m,” then the total time taken is O(m + n), with a linear auxiliary space. It is worth noting that the time and auxiliary space of this algorithm is the same as the KMP algorithm, but this particular algorithm is simpler to comprehend. In this approach, we create a Z array as part of the process.

What is Z Array?
For a string str[0..n-1], Z array is of same length as string. An element Z[i] of Z array stores length of the longest substring starting from str[i] which is also a prefix of str[0..n-1]. The first entry of Z array is meaning less as complete string is always prefix of itself.

Example:
Index            0   1   2   3   4   5   6   7   8   9  10  11
Text             a   a   b   c   a   a   b   x   a   a   a   z
Z values         X   1   0   0   3   1   0   0   2   2   1   0
More Examples:
str  = "aaaaaa"
Z[]  = {x, 5, 4, 3, 2, 1}
str = "aabaacd"
Z[] = {x, 1, 0, 2, 1, 0, 0}
str = "abababab"
Z[] = {x, 0, 6, 0, 4, 0, 2, 0}


How is Z array helpful in Searching Pattern in Linear time?
The idea is to concatenate pattern and text, and create a string “P$T” where P is pattern, $ is a special character should not be present in pattern and text, and T is text. Build the Z array for concatenated string. In Z array, if Z value at any point is equal to pattern length, then pattern is present at that point.

Example:
Pattern P = "aab",  Text T = "baabaa"
The concatenated string is = "aab$baabaa"
Z array for above concatenated string is {x, 1, 0, 0, 0,
3, 1, 0, 2, 1}.
Since length of pattern is 3, the value 3 in Z array
indicates presence of pattern.

How to construct Z array?
A Simple Solution is to run two nested loops, the outer loop goes to every index and the inner loop finds length of the longest prefix that matches the substring starting at the current index. The time complexity of this solution is O(n2).
We can construct Z array in linear time.

The idea is to maintain an interval [L, R] which is the interval with max R
such that [L,R] is prefix substring (substring which is also prefix).
Steps for maintaining this interval are as follows –
1) If i > R then there is no prefix substring that starts before i and
                                                                 ends after i, so we reset L and R and compute new [L,R] by comparing
str[0..] to str[i..] and get Z[i] (= R-L+1).
2) If i <= R then let K = i-L,  now Z[i] >= min(Z[K], R-i+1)  because
str[i..] matches with str[K..] for atleast R-i+1 characters (they are in
[L,R] interval which we know is a prefix substring).
Now two sub cases arise –
a) If Z[K] < R-i+1  then there is no prefix substring starting at
str[i] (otherwise Z[K] would be larger)  so  Z[i] = Z[K]  and
interval [L,R] remains same.
b) If Z[K] >= R-i+1 then it is possible to extend the [L,R] interval
thus we will set L as i and start matching from str[R]  onwards  and
get new R then we will update interval [L,R] and calculate Z[i] (=R-L+1).

For better understanding of above step by step procedure please check this animation – http://www.utdallas.edu/~besp/demo/John2010/z-algorithm.htm
The algorithm runs in linear time because we never compare character less than R and with matching we increase R by one so there are at most T comparisons. In mismatch case, mismatch happen only once for each i (because of which R stops), that’s another at most T comparison making overall linear complexity.

Below is the implementation of Z algorithm for pattern searching.
'''
# Python3 program that implements Z algorithm
# for pattern searching

# Fills Z array for given string str[]
def getZarr(string, z):
    n = len(string)

    # [L,R] make a window which matches
    # with prefix of s
    l, r, k = 0, 0, 0
    for i in range(1, n):

        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > r:
            l, r = i, i

            # R-L = 0 in starting, so it will start
            # checking from 0'th index. For example,
            # for "ababab" and i = 1, the value of R
            # remains 0 and Z[i] becomes 0. For string
            # "aaaaaa" and i = 1, Z[i] and R become 5
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:

            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - l

            # if Z[k] is less than remaining interval
            # then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5
            # and L = 2
            if z[k] < r - i + 1:
                z[i] = z[k]

            # For example str = "aaaaaa" and i = 2,
            # R is 5, L is 0
            else:

                # else start from R and check manually
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

# prints all occurrences of pattern
# in text using Z algo
def search(text, pattern):

    # Create concatenated string "P$T"
    concat = pattern + "$" + text
    l = len(concat)

    # Construct Z array
    z = [0] * l
    getZarr(concat, z)

    # now looping through Z array for matching condition
    for i in range(l):

        # if Z[i] (matched region) is equal to pattern
        # length we got the pattern
        if z[i] == len(pattern):
            print("Pattern found at index",
                  i - len(pattern) - 1)

# Driver Code
if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    search(text, pattern)

# This code is contributed by
# sanjeev2552
"""
    Output:

Pattern found at index 0
Pattern found at index 10
Time Complexity: O(m+n), where m is length of pattern and n is length of text.

Auxiliary Space: O(n)
"""