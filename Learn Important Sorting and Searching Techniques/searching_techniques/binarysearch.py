num  = [1,2,4,5,6,8,12,14,66]

target = int(input("What's the target: "))

size = len(num)

low =0

high = size -1

while low<=high:
    mid = low + (high-low)//2
    
    if num[mid] == target:
        print("Found")
        break
    elif num[mid] > target:
        high = mid -1
    else:
        low = mid +1
else:
    print("Not Found")
