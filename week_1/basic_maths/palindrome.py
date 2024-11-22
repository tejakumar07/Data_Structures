# This Program is About Checking the Palindrome Number
# It is the LeetCode Problem
# Problem Link : https://leetcode.com/problems/palindrome-number/description/
# This is similar to the Reverse Number when we comare it with the Orginal Number
# If they Both are Match then it is the Palindrome number if not is not a palindrome number

def check_palindrome(number):
    orginal_number = number
    reversal_number = 0
    while number > 0:
        last_digit = number % 10
        number = int(number / 10)
        reversal_number = (reversal_number * 10) + last_digit
    if reversal_number == orginal_number :
        return True
    else:
        return False 

if __name__ == "__main__":
    number = int(input("What's N: "))
    print(check_palindrome(number))