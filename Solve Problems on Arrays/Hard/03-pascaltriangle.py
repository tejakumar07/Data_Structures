# Type - 2 
# Optimal Solution

def teja(n):
    ans = 1
    print(ans, end=" ")
    for i in range(1, n + 1):
        ans = ans * (n - i + 1) // i
        print(ans, end= " ")
if __name__ == "__main__":
    teja(5)