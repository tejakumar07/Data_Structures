# Sum of first N Natural Numbers
# 2.Functional way

def function(n):
    if n == 0:
        return 0
    return n + function(n-1)

if __name__ == "__main__":
    n = int(input("N: "))
    print(function(n))