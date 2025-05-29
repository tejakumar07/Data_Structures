# Only Sorted Array
class Arrays:
    def __init__(self, arr):
        self.arr = arr
    def RemoveDuplicates(self):
        unique = set()
        for i in range(len(arr)):
            unique.add(arr[i])
        unique = list(unique)
        for i in range(len(unique)):
            self.arr[i] = unique[i]
        return self.arr

if __name__ == "__main__":
    arr = [1,2,2,3,3,3,4,4,5,5,5,6,7,7,8,9,10]
    teja = Arrays(arr)
    print(teja.RemoveDuplicates())
