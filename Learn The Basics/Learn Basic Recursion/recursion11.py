# Reversing the list using recursion
def function(start,end):
    if start >= end:
        return
    a[start],a[end] = a[end],a[start]
    function(start+1,end-1)
if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    end = len(a)-1
    function(0,end)
    print(a)