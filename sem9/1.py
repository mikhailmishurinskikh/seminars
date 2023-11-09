tokens = list(input())
tokens = tokens[::-1]
operators = {'-': 1, '+': 2, '/': 3, '*':4}
op_stack = []
output = []
while tokens != []:
    token = tokens.pop()
    if token in operators.keys():
        while (op_stack != [] and op_stack[-1] not in ['(',')']
            and operators[op_stack[-1]] > operators[token]):
            output += [op_stack.pop()]
        op_stack += [token]
    elif token == '(':
        op_stack += [token]
    elif token == ')':
        while op_stack[-1] != '(':
            output += [op_stack.pop()]
        op_stack.pop()
    else:
        output.append(token)

while op_stack != []:
    output.append(op_stack.pop())
print(output)
