# Brute Force Approach

from typing import List
import math

def hours_needed(piles: List[int], eating_speed: int) -> int:
    total_hours = 0
    for pile in piles:
        total_hours += math.ceil(pile / eating_speed)
    return total_hours

def min_eating_speed(piles: List[int], h: int) -> int:
    max_pile = max(piles)
    for speed in range(1, max_pile + 1):
        if hours_needed(piles, speed) <= h:
            return speed

piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))
