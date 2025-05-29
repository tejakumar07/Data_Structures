# The Last Program will work for only the +VE integers
# Let's Fix this in this Code

def divisiors(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
            factors.append(-i)
            factors.sort()
    return factors

if __name__ == "__main__":
    n = int(input("What's N: "))
    n = abs(n)
    print(divisiors(n))