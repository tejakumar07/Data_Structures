# Optimal Approach
class Arrays:
    def __init__(self, arr):
        self.arr = arr
    def SecondLargest(self):
        largest = self.arr[0]
        slargest = float('-inf')
        for i in range(1, len(self.arr)):
            if self.arr[i] > largest:
                slargest = largest
                largest = self.arr[i]
            elif self.arr[i] > slargest and self.arr[i] < largest:
                slargest = self.arr[i]
        print(f"The Second Largest Element is: {slargest}")
    def SecondSmallest(self):
        smallest = self.arr[0]
        ssmallest = float('inf')
        for i in range(1, len(self.arr)):
            if self.arr[i] < smallest:
                ssmallest = smallest
                smallest = self.arr[i]
            elif self.arr[i] < ssmallest and self.arr[i] > smallest:
                ssmallest = self.arr[i]
        print(f"The Second Smallest Element is: {ssmallest}")

if __name__ == "__main__":
    arr = [2,1,8,10,4,60,100,420,69,92]
    teja = Arrays(arr)
    teja.SecondLargest()
    teja.SecondSmallest()
