def sum_of_subarray_ranges(nums):
    n = len(nums)
    total_sum = 0

    for start in range(n):
        for end in range(start, n):
            min_val = float('inf')
            max_val = float('-inf')
            
            for i in range(start, end+1):
                min_val = min(min_val, nums[i])
                max_val = max(max_val, nums[i])
            
            total_sum += max_val - min_val

    return total_sum

nums = [1,2,3]
result = sum_of_subarray_ranges(nums)
print("Output:", result)
