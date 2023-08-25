def asteroid_collision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
                continue
            elif abs(asteroid) == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    
    return stack

# Example usage
asteroids = [5, 10, -5]
result = asteroid_collision(asteroids)
print(result)  # Output: [5, 10]
