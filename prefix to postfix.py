def is_operator(char):
    return char in "+-*/"

def prefix_to_postfix(prefix_expression):
    stack = []
    for char in reversed(prefix_expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            postfix = operand1 + operand2 + char
            stack.append(postfix)
        else:
            stack.append(char)
    return stack[0]

prefix_expression = "/A+BC"
postfix_expression = prefix_to_postfix(prefix_expression)
print("Prefix Expression:", prefix_expression)
print("Postfix Expression:", postfix_expression)
