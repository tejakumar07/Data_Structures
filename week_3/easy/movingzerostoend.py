# Brute Force Approach
# Moving Zeros to End.
def movingZeros(arr,n):
    temp = []
    for i in range(0,n):
        if arr[i] != 0:
            temp.append(arr[i])
    for i in range(0,len(temp)):
        arr[i] = temp[i]
    for i in range(len(temp),n):
        arr[i] = 0
    return arr
def main():
    arr = [1,0,3,2,0,0,0,5,7,9,6,0,4,0,3,2,1,0]
    n = len(arr)
    print(f"After moving zeros: {movingZeros(arr,n)}")    
if __name__ == "__main__":
    main()

