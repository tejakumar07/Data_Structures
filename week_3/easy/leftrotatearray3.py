def lRotate(arr,n):
    d = int(input("D: "))
    d = d % n
    if d == 0:
        return arr
    # Rotate [1, 2, 3, 4, 5] by d = 2
    # arr[d:] Take from index 2 onward: [3, 4, 5]
    # arr[:d] Take the first 2 elements: [1, 2]

    return arr[d:] + arr[:d]
def main():
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    print(f"After Rotating: {lRotate(arr,n)}")
if __name__ == "__main__":
    main()
