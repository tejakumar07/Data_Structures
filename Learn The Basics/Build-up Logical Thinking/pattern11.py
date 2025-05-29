# This is another Pattern
"""
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
"""

n = int(input("What's N: "))
space = 2 * (n - 1)

for i in range(1, n + 1):
    # Print the first increasing sequence
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print spaces in the middle
    for _ in range(space):
        print(" ", end="")
    space -= 2  # Reduce spaces as rows increase

    # Print the second decreasing sequence
    for j in range(i, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print("")
