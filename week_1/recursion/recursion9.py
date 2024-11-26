# Similar to the Last Program for sum of N natural Numbers
# let's try for the factorial

def function(n):
    if n == 1:
        return 1
    return n * function(n-1)

if __name__ == "__main__":
    n = int(input("N: "))
    print(function(n))