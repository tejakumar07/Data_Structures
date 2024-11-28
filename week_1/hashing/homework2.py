'''
Find the highest/lowest frequency element


Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Pre-requisite: Hashing Theory and  Counting frequencies of array elements

Examples:

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

'''
# Asked to Solve using 2 Methods

# Method - I (Brute-Force approach(Using two loops):)
def fetching(array, query):
    memory = {}

    # Count the frequency of each element in the array
    for num in array:
        if num in memory:
            memory[num] += 1
        else:
            memory[num] = 1

    # Initialize variables for highest and lowest frequency
    highest_frequency = float('-inf')
    lowest_frequency = float('inf')
    highest_element = None
    lowest_element = None

    # Traverse the frequency map to find the highest and lowest frequencies
    for num, freq in memory.items():
        if freq > highest_frequency:
            highest_frequency = freq
            highest_element = num
        if freq < lowest_frequency:
            lowest_frequency = freq
            lowest_element = num

    return highest_element, highest_frequency, lowest_element, lowest_frequency


if __name__ == "__main__":
    array = [10, 5, 10, 15, 10, 5]
    query = list(map(int, input("Enter query elements: ").split()))
    highest, highest_freq, lowest, lowest_freq = fetching(array, query)

    print(f"Highest frequency element: {highest} with frequency: {highest_freq}")
    print(f"Lowest frequency element: {lowest} with frequency: {lowest_freq}")
