# Print 1 to N using Recursion

def function(i,n):
    if i > n:
        return
    print(i)
    function(i+1,n)
if __name__ == "__main__":
    num = int(input("What's N: "))
    function(1,num)