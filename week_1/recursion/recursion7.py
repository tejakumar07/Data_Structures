# Sum of first N Natural Numbers
# 1. Parameterized way
def function(i,sum):
    if i < 0:
        print(sum)
        return
    function(i-1,sum+i)
if __name__ == "__main__":
    n = int(input("N: "))
    function(n,0)