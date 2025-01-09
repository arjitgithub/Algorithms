'''Naive algorithm for Pattern Searching

Given text string with length n and a pattern with length m, the task is to prints all occurrences of pattern in text.
Note: You may assume that n > m.

Examples:

Input:  text = “THIS IS A TEST TEXT”, pattern = “TEST”
Output: Pattern found at index 10



Input:  text =  “AABAACAADAABAABA”, pattern = “AABA”
Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12




Pattern searching

Naive Pattern Searching algorithm:
Slide the pattern over text one by one and check for a match. If a match is found, then slide by 1 again to check for subsequent matches.

'''


def search_pattern(pattern, text):
    # Get the lengths of the pattern and the text
    m = len(pattern)
    n = len(text)

    # A loop to slide pattern over text one by one
    for i in range(n - m + 1):
        # For current index i, check for pattern match
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        # If the entire pattern matches the text starting at index i
        if j == m:
            print(f"Pattern found at index {i}")

# Example usage
if __name__ == "__main__":
    # Example 1
    text1 = "AABAACAADAABAABA"
    pattern1 = "AABA"
    print("Example 1:")
    search_pattern(pattern1, text1)

    # Example 2
    text2 = "agd"
    pattern2 = "g"
    print("\nExample 2:")
    search_pattern(pattern2, text2)
"""
Output
Pattern found at index 0
Pattern found at index 9
Pattern found at index 13
Time Complexity: O(N2)
Auxiliary Space: O(1)

Complexity Analysis of Naive algorithm for Pattern Searching:
    Best Case: O(n)
When the pattern is found at the very beginning of the text (or very early on).
The algorithm will perform a constant number of comparisons, typically on the order of O(n) comparisons, where n is the length of the pattern.
Worst Case: O(n2)
When the pattern doesn’t appear in the text at all or appears only at the very end.
The algorithm will perform O((n-m+1)*m) comparisons, where n is the length of the text and m is the length of the pattern.
In the worst case, for each position in the text, the algorithm may need to compare the entire pattern against the text.
"""