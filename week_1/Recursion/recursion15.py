# This is also the Fibonacci Number
# This can be done using multiple recursion

def function(n):
    if n <= 1:
        return n
    last = function(n-1)
    slast = function(n-2)
    return last + slast

if __name__ == "__main__":
    n = int(input("What's N: "))
    print(function(n))