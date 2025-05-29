# Method - II using Hash Map

def highest_lowest_frequency(arr):
    # Step 1: Create a frequency map
    freq_map = {}
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    # Step 2: Initialize variables for highest and lowest frequency
    highest_freq = float('-inf')
    lowest_freq = float('inf')
    highest_element = None
    lowest_element = None
    
    # Step 3: Traverse the frequency map to find highest and lowest frequencies
    for num, freq in freq_map.items():
        if freq > highest_freq:
            highest_freq = freq
            highest_element = num
        if freq < lowest_freq:
            lowest_freq = freq
            lowest_element = num
    
    # Step 4: Return the result
    return highest_element, lowest_element

if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]  # Example input
    highest, lowest = highest_lowest_frequency(arr)
    print(f"Highest Frequency Element: {highest}")
    print(f"Lowest Frequency Element: {lowest}")
