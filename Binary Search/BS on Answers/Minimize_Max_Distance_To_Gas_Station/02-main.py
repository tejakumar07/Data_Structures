import heapq  # For using priority queue (heap)

def minimiseMaxDistance(positions, extraStations):
    numStations = len(positions)
    
    # This list tracks how many extra gas stations are added in each segment
    gasStationsInSegment = [0] * (numStations - 1)

    # Priority queue (max heap) to keep track of largest segment
    # We'll push (-segmentLength, index), to simulate max-heap using min-heap
    maxHeap = []

    # Step 1: Add all segments into heap
    for i in range(numStations - 1):
        segmentLength = positions[i + 1] - positions[i]
        heapq.heappush(maxHeap, (-segmentLength, i))

    # Step 2: Place each extra gas station
    for _ in range(extraStations):
        # Pop the largest segment
        negLength, segmentIndex = heapq.heappop(maxHeap)

        # Increase the number of gas stations in that segment
        gasStationsInSegment[segmentIndex] += 1

        # Recalculate the new largest distance in that segment
        originalLength = positions[segmentIndex + 1] - positions[segmentIndex]
        parts = gasStationsInSegment[segmentIndex] + 1  # original segment + new stations
        newMaxSegment = originalLength / parts

        # Push the updated segment back into heap
        heapq.heappush(maxHeap, (-newMaxSegment, segmentIndex))

    # The top of the heap now contains the maximum segment length (negated)
    minPossibleMaxDist = -maxHeap[0][0]
    return minPossibleMaxDist

if __name__ == "__main__":
    # Test case
    positions = [1, 2, 3, 4, 5]
    extraStations = 4
    answer = minimiseMaxDistance(positions, extraStations)
    print("The answer is:", answer)
