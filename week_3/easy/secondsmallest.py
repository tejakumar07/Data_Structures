def main():
    arr = list(map(int,input("List: ").split()))
    n = len(arr)
    print(f"The Enter List is: {arr}")
    print(f"The Smallest and Second Smallest Numbers are: {sSmallest(arr,n)}")
def sSmallest(arr,n):
    small = arr[0]
    ssmall = float('inf')
    for i in range(n):
        if arr[i] < small:
            ssmall = small
            small = arr[i]
        elif arr[i] > small and arr[i] < ssmall:
            ssmall = arr[i]
    return small,ssmall
if __name__ == "__main__":
    main()