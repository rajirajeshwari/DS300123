def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '%', '^'])
    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '+':
                stack.append(num1 + num2)
            elif char == '-':
                stack.append(num1 - num2)
            elif char == '*':
                stack.append(num1 * num2)
            elif char == '/':
                stack.append(num1 / num2)
            elif char == '%':
                stack.append(num1 % num2)
            elif char == '^':
                stack.append(num1 ** num2)
    return stack.pop()
postfix_expression = "235*+"
result = evaluate_postfix(postfix_expression)
print(result)
