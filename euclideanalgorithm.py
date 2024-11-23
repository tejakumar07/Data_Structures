# This code is about GCD but solving using Euclidean Algorithm
# Euclidean Algorithm Proof for GCD is : gcd(a,b) = gcd(a-b,b) where a > b

# Function to calculate GCD using Euclidean algorithm
def gcd(a, b):
    # Continue looping until b becomes 0
    while b != 0:
        # Update a to be the value of b, and b to be the remainder of a divided by b
        a, b = b, a % b
    # Once b is 0, a will contain the GCD
    return a

# Take user input for the two numbers
a = int(input())  # First number
b = int(input())  # Second number

# Call the gcd function and store the result in the variable 'hcf'
hcf = gcd(a, b)

# Output the GCD (HCF) value
print(hcf)

