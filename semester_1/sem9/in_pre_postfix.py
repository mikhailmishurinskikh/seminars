data_pre = list(input())
data_post = data_pre[::-1]
def deystra(tokens, p):
    if p == 'post':
        operators = {'-': 1, '+': 2, '/': 3, '*':4}
    elif p == 'pre':
        operators = {'-': 2, '+': 1, '/': 4, '*':3}
    op_stack = []
    output = []
    while tokens != []:
        token = tokens.pop()
        if token in ['(', ')'] and p == 'pre':
            if token == '(': token = ')'
            else: token = '('
        if token in operators.keys():
            while (op_stack != [] and op_stack[-1] not in ['(',')']
                and operators[op_stack[-1]] >= operators[token]):
                output.append(op_stack.pop())
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
    if p == 'pre':
        output = output[::-1]
    output = ''.join(output)
    return output
print('postfix: ', deystra(data_post, 'post'))
print('prefix: ', deystra(data_pre, 'pre'))
