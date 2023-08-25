def removeKdigits(num, k):
    n = len(num)
    
    if k == n:
        return "0"
    
    min_num = float('inf')
    for i in range(n - k + 1):
        new_num = num[:i] + num[i+k:]
        min_num = min(min_num, int(new_num))
    
    return str(min_num)

num = "1432219"
k = 3
output = removeKdigits(num, k)
print(output)  # Output: "1219"
