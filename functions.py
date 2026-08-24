nums = []
mean = 0

def calculate_mean(nums):
    global mean
    total = sum(nums)
    count = len(nums)
    if count == 0:
        return 0
    mean = total / count
    return mean

def calculate_median(nums):
    global median
    sorted_nums = sorted(nums) #sort nums in ascending order
    count = len(sorted_nums) 
    if count == 0:
        return 0
    mid = count // 2
    if count % 2 == 0: #if no exact middle value, average the two middle values
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 #average middle values
    else:
        median = sorted_nums[mid]
    return median

def calculate_mode(nums):
    global mode
    frequency = {} #dictionary to save frequency of each number
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1 #increment frequency count for each number
    max_freq = max(frequency.values(), default=0) #find the maximum frequency of any number in the list
    modes = [num for num, freq in frequency.items() if freq == max_freq] #list of numbers that have the maximum frequency
    if len(modes) >1:
        sorted_modes = sorted(modes) #sort the modes in ascending order
        mode = sorted_modes[0] #return the smallest mode if there are multiple modes
    if len(modes) == len(frequency): 
        return None  # No mode if all numbers are unique
    return modes


mean = calculate_mean(nums)
median = calculate_median(nums)
mode = calculate_mode(nums)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
