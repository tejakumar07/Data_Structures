# This is another example for the Recursion
# This is about Factorial

def factorial(n):
    if n == 0:
        return
    else:
        return n * (n-1)
if __name__ == "__main__":
    n = int(input("What's N: "))
    print(factorial(n))
    