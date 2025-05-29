# Optimal Approach
class Arrays:
    def __init__(self,arr):
        self.arr = arr
    def remove_duplicates(self):
        i = 0
        for j in range(1, len(self.arr)):
            if self.arr[j] != self.arr[i]:
                self.arr[i+1] = self.arr[j]
                i += 1
        print(*self.arr)
        return i+1

if __name__ == "__main__":
    arr = [1,1,1,3,4,4,7,7,7,9,10,10,10]
    teja = Arrays(arr)
    print(teja.remove_duplicates())
