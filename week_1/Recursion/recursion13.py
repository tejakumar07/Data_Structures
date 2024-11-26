# Check if a string is palindrome or not
# It is a LeetCode Problem
# Link: https://leetcode.com/problems/valid-palindrome/description/
def check_palindrome(i,n):
    if i >= n//2:
        return True
    if name[i] != name[n-i-1]:
        return False
    return check_palindrome(i+1,n)

if __name__ == "__main__":
    name = input("Enter the name: ")
    n = len(name)
    print(check_palindrome(1,n))