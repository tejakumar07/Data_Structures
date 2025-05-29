class Array:
    def __init__(self, arr):
        self.arr = arr
    def check_array_sorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True


if __name__ == "__main__":
    arr = [x for x in map(int, input("Array: ").split())]
    teja = Array(arr)
    print(teja.check_array_sorted())
