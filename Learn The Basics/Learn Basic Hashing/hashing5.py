name = input("Enter the Name: ")
length = len(name)
query = input("Enter the Query Here: ")

# Declaring the Hash Array For all the Lower Case Letters
hash = [0] * 26

for i in range(length):
    if 'a' <= name[i] <= 'z':
        hash[ord(name[i]) - ord('a')] += 1

for q in query:
    if 'a' <= q <= 'z':
        print(hash[ord(q) - ord('a')])
    else:
        print(0)


"""
What is ord()?
ord() gives the ASCII value of a character.
Example:
ord('a') → 97
ord('b') → 98
ord('c') → 99
Why use ord(char) - ord('a')?
We use this to find the position of a lowercase letter ('a' to 'z') in the alphabet:

'a' is the 1st letter (position 0 in programming).
'b' is the 2nd letter (position 1 in programming).
'c' is the 3rd letter (position 2 in programming).
Formula:
ord(char) - ord('a') gives the position of the letter.

Example:
ord('a') - ord('a') = 97 - 97 = 0 (position of 'a')
ord('b') - ord('a') = 98 - 97 = 1 (position of 'b')
ord('z') - ord('a') = 122 - 97 = 25 (position of 'z')
"""