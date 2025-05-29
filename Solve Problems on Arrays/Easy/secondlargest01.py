# Better Solution
class Arrays:
    def __init__(self, arr):
        self.arr = arr
    def Largest(self):
        largest = self.arr[0]
        for i in range(1, len(self.arr)):
            if self.arr[i] > largest:
                largest = self.arr[i]
        self.Secondlargest(largest)
    def Secondlargest(self, largest):
        slargest = float('-inf')
        for i in range(0, len(self.arr)):
            if self.arr[i] > slargest and self.arr[i] < largest:
                slargest = self.arr[i]
        print(slargest)

if __name__ == "__main__":
    arr = [x for x in map(int, input("Array: ").split())]
    teja = Arrays(arr)
    teja.Largest()
