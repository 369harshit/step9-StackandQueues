def count_greater_elements(arr, index):
    n = len(arr)
    count = 0
    
    for i in range(index, n):
        if arr[i] > arr[index]:
            count += 1
    
    return count

# Example usage
input_array = [5,2,10,4]
indices = [0, 1]

for index in indices:
    result = count_greater_elements(input_array, index)
    print(result, end=" ")  
