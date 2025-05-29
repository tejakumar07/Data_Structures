# Reversing an array without recursion
# Method - I
a = [1,2,3,4,5]

start = 0
end = len(a) -1

while start < end:
    a[start],a[end] = a[end],a[start]
    start+=1
    end-=1
print(a)

# Method - II

b = [6,7,8,9,10]

b.reverse()

print(b)
