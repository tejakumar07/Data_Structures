# This code is similar to the alldivisiors.py
# The Time Complexity is more in the previous code
# Let's Fix this in this mode of code
import math

def divisiors(n):
    factors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    return sorted(factors)

if __name__ == "__main__":
    n = int(input("What's N: "))
    print(divisiors(n))

