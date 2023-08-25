def is_operator(char):
    return char in "+-*/"

def prefix_to_infix(prefix_expression):
    stack = []
    for char in reversed(prefix_expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f"({operand1} {char} {operand2})"
            stack.append(infix)
        else:
            stack.append(char)
    return stack[0]

prefix_expression = "/-ab+-cde"
infix_expression = prefix_to_infix(prefix_expression)
print("Prefix Expression:", prefix_expression)
print("Infix Expression:", infix_expression)
