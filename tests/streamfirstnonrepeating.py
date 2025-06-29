# Problem Statement:
# Given an input stream s consisting only of lowercase alphabets. While reading characters from the stream, you have to tell which character has appeared only once in the stream upto that point. If there are many characters that have appeared only once, you have to tell which one of them was the first one to appear. If there is no such character then append '#' to the answer.

# NOTE:
# 1. You need to find the answer for every i (0 <= i < n)
# 2. In order to find the solution for every you need to consider the string from starting position till the ith position.
 

# Example 1:

# Input: s = "aabc"

# Output: "a#bb"

# Explanation: For every ith character we will consider the string from index 0 till index i first non repeating character is as follow- "a" - first non-repeating character is 'a' "aa" - no non-repeating character so '#' "aab" - first non-repeating character is 'b' "aabc" - there are two non repeating characters 'b' and 'c',  first non-repeating character is 'b' because 'b' comes before 'c' in the stream.




# Example 2:

# Input: s = "zz"

# Output: "z#"

# Explanation: For every character first non repeating character is as follow- "z" - first non-repeating character is 'z' "zz" - no non-repeating character so '#'




from collections import deque, Counter

def first_non_repeating(s):
    count = Counter()
    q = deque()
    result = []

    for ch in s:
        count[ch] += 1
        q.append(ch)

        # Remove characters from the front of the queue until the front is non-repeating
        while q and count[q[0]] > 1:
            q.popleft()

        if q:
            result.append(q[0])
        else:
            result.append('#')

    return ''.join(result)

# Input
s = input().strip()
print(first_non_repeating(s))