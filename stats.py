"""
Lab 1: The Multi-Paradigm Tour -- Python implementation.

Run: python stats.py 4 8 15 16 23 42
Complete compute_stats() below. See the assignment,
Part B, for the full shared contract (all three language versions
must match it exactly).
"""

import sys
from typing import List, Tuple


def compute_stats(nums: List[int]) -> Tuple[float, float, int]:
    """
    Return (mean, median, mode).
    - median: for an even count, average the two middle values after sorting.
    - mode: the most frequent value; on a tie, the SMALLEST tied value.
    """

    mean = 0
    total = sum(nums)
    count = len(nums)
    if count == 0:
        mean = 0
    else:
        mean = total / count

    median = 0
    sorted_nums = sorted(nums) #sort nums in ascending order
    count = len(sorted_nums) 
    if count == 0:
        median = 0
    else:
        mid = count // 2
        if count % 2 == 0: #if no exact middle value, average the two middle values
            median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 #average middle values
        else:
            median = sorted_nums[mid]

    mode = 0
    frequency = {} #dictionary to save frequency of each number
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1 #increment frequency count for each number
    max_freq = max(frequency.values(), default=0) #find the maximum frequency of any number in the list
    modes = [num for num, freq in frequency.items() if freq == max_freq] #list of numbers that have the maximum frequency
    if len(modes) >1:
        sorted_modes = sorted(modes) #sort the modes in ascending order
        mode = sorted_modes[0] #return the smallest mode if there are multiple modes
    if len(modes) == len(frequency): 
        mode = None  # No mode if all numbers are unique
    
    return (mean, median, mode)
    # TODO
    raise NotImplementedError


def main() -> int:
    if len(sys.argv) < 2:
        return 1
    nums = [int(a) for a in sys.argv[1:]]
    mean, median, mode = compute_stats(nums)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
