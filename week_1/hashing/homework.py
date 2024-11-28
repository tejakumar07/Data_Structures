'''
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array
'''

# Asked to solve using 2 methods

# Method - I using Loop

def frequency_range(target,size):
    for t in target:
        count = 0
        for i in range(size):
            if array[i] == t:
                count += 1
        print(f"The {t} is repeated {count} times")

if __name__ == "__main__":
    array = [1,3,4,5,7,34,43,1,7,9,7,9,3,12,52]
    size = len(array)
    target = list(map(int,input("Target List: ").split()))
    frequency_range(target,size)