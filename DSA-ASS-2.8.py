def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ''
    while len(stack) > 0:
        reversed_str += stack.pop()
    return reversed_str
s = 'Hello, world!'
result = reverse_string(s)
print(result)
