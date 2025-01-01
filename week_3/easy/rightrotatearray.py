#  if arr = [1, 2, 3, 4, 5] and d = 2
# arr[-d:] becomes arr[-2:], which gives [4, 5].
# arr[:-d] becomes arr[:-2], which gives [1, 2, 3]

def rRotate(arr,n):
    d = int(input("D: "))
    d = d % n
    if d == 0:
        return arr
    return arr[-d:] + arr[:-d]
def main():
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    print(f"After Rotating: {rRotate(arr,n)}")
if __name__ == "__main__":
    main()