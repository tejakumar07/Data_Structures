# Print N to 1 using Recursion

def function(n,i):
    if n < i:
        return
    
    print(n)
    function(n-1,i)

if __name__ == "__main__":
    num = int(input("What's N: "))
    function(num,1)