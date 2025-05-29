class Arrays:
    def __init__(self, arr):
        self.arr = arr
    keys = []
    def remove_duplicates(self):
        key = []
        for i in range(len(self.arr)):
            if self.arr[i] not in key:
                key.append(arr[i])
        for i in range(len(key)):
            arr[i] = key[i]
        print(len(key))
        return arr

if __name__ == "__main__":
    arr = [1,1,1,2,3,3,4,4,5,7,7,9]
    teja = Arrays(arr)
    print(teja.remove_duplicates())
