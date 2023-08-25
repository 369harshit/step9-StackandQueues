def is_operator(char):
    return char in "+-*/"

def postfix_to_infix(postfix_expression):
    stack = []
    for char in postfix_expression:
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix = f"({operand1} {char} {operand2})"
            stack.append(infix)
        else:
            stack.append(char)
    return stack[0]

postfix_expression = "ab+c+"
infix_expression = postfix_to_infix(postfix_expression)
print("Postfix Expression:", postfix_expression)
print("Infix Expression:", infix_expression)
