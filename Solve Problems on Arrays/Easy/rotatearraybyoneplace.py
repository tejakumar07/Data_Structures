class Arrays:
    def __init__(self, arr):
        self.arr = arr
    def rotate_array_by_one_place(self):
        temp = arr[0]
        for i in range(1, len(self.arr)):
            self.arr[i-1] = self.arr[i]
        self.arr[-1] = temp
        return f"After Rotating Array by 1 place {self.arr}"
if __name__ == "__main__":
    arr = [int(x) for x in map(int, input("Array: ").split())]
    print(f"Orginal Array is: {arr}")
    teja = Arrays(arr)
    print(teja.rotate_array_by_one_place())
