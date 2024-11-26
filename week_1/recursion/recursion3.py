# This is another Example for Recursion in FibonacciSequence

def FibonacciSequence(n):
    # Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciSequence(n-1) + FibonacciSequence(n-2)

if __name__ == "__main__":
    num = int(input("What's N: "))
    print(FibonacciSequence(num))
# time complexity 𝑂(2𝑛).

# The Code will not work for the 3 digits ex: 100

"""
def FibonacciSequence(n, memo={}):
    if n in memo:  # Return cached result
        return memo[n]
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case with memoization
        memo[n] = FibonacciSequence(n-1, memo) + FibonacciSequence(n-2, memo)
        return memo[n]

if __name__ == "__main__":
    num = int(input("What's N: "))
    print(FibonacciSequence(num))

"""

"""
from functools import lru_cache

@lru_cache(maxsize=None)  # Cache results of function calls
def FibonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciSequence(n-1) + FibonacciSequence(n-2)

if __name__ == "__main__":
    num = int(input("What's N: "))
    print(FibonacciSequence(num))

"""