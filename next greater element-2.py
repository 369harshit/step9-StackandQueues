def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
    
    return result

nums = [1, 2, 1]
output = next_greater_element(nums)
print("Output:", output)
