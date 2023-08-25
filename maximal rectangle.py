def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    # To handle edge case when entire row is filled with 1's
    heights = [0] * (cols + 1)
    max_area = 0

    for row in matrix:
        for i in range(cols):
            if row[i] == "1":
                heights[i] = heights[i] + 1
            else:
                0

        stack = []
        for i in range(cols + 1):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]]

print(maximalRectangle(matrix))
