def sum_of_subarray_minimums(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        min_val = float('inf')
        for j in range(i, n):
            min_val = min(min_val, arr[j])
            total_sum += min_val

    return total_sum

arr = [3,1,2,4]
result = sum_of_subarray_minimums(arr)
print(result)
