# It is the LeetCode Problem
# Link : https://leetcode.com/problems/armstrong-number/description/
import math

def armstrong_number(n):
    """
    Armstrong Number:
    An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum 
    of its own digits each raised to the power of the number of digits.
    
    Example Armstrong Numbers:
    - 153: 1^3 + 5^3 + 3^3 = 153 (Armstrong)
    - 9474: 9^4 + 4^4 + 7^4 + 4^4 = 9474 (Armstrong)
    - 370: 3^3 + 7^3 + 0^3 = 370 (Armstrong)
    
    Non-Armstrong Number Example:
    - 123: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 (Not Armstrong)
    """

    count = int(math.log10(n) + 1)  # Calculate the number of digits in the number
    original_number = n  # Store the original number for comparison
    sum = 0  # Initialize the sum to 0

    # Loop through each digit of the number
    while n > 0:
        last_digit = n % 10  # Extract the last digit
        n = int(n / 10)  # Remove the last digit from the number
        sum = sum + pow(last_digit, count)  # Add the digit raised to the power of 'count' to the sum

    # After the loop, compare the sum of the digits raised to the power of count with the original number
    return original_number == sum  # Return True if the sum is equal to the original number, else False

if __name__ == "__main__":
    n = int(input("Enter the Number: "))  # Take input from the user
    print(armstrong_number(n))  # Output True if the number is an Armstrong number, otherwise False
