# This is the LeetCode Question
# Problem Link : https://leetcode.com/problems/reverse-integer/description/

def reverse_function(n):
    # Step 1: Initialize a variable to store the reversed number.
    # This starts as 0 because we will build the reversed number from scratch.
    reverse_number = 0

    # Step 2: Use a loop to process each digit of the number.
    # The loop runs as long as the number 'n' is greater than 0.
    while n > 0:
        # Step 3: Extract the last digit of the number using the modulo operator.
        # Example: If n = 123, last_digit = 123 % 10 = 3
        last_digit = n % 10

        # Step 4: Update the reverse_number by shifting its digits left (multiply by 10)
        # and adding the last_digit to the rightmost position.
        # Example: If reverse_number = 12 and last_digit = 3, 
        # reverse_number becomes 12 * 10 + 3 = 123
        reverse_number = (reverse_number * 10) + last_digit

        # Step 5: Remove the last digit from the original number.
        # This is done by integer division (//), which drops the remainder.
        # Example: If n = 123, n = 123 // 10 = 12
        n = int(n / 10)  # Alternatively, you could write 'n //= 10'

    # Step 6: After the loop ends, the reversed number is fully built.
    # Return the reversed number so it can be used or displayed.
    return reverse_number

if __name__ == "__main__":
    # Step 7: Take input from the user.
    # Convert the input (which is a string) into an integer using int().
    number = int(input("Enter the Number: "))

    # Step 8: Call the reverse_function with the user's input and print the result.
    # The function will return the reversed version of the input number.
    print("The Reverse Number is: ", reverse_function(number))
