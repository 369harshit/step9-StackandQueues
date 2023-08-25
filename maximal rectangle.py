def maximalRectangle(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                # Calculate the maximum width of the rectangle
                width = 1
                while j + width < cols and matrix[i][j + width] == '1':
                    width += 1
                
                # Calculate the maximum height of the rectangle
                height = 1
                for k in range(i + 1, rows):
                    valid_height = True
                    for l in range(j, j + width):
                        if matrix[k][l] != '1':
                            valid_height = False
                            break
                    if valid_height:
                        height += 1
                    else:
                        break
                
                # Calculate and update the maximum area
                area = width * height
                max_area = max(max_area, area)
    
    return max_area

# Example usage
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

print(maximalRectangle(matrix))  # Output should be 6
