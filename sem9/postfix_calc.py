def calc(a, b, oper):
    if oper == '+': return a+b
    elif oper == '-': return a-b
    elif oper == '*': return a*b
    elif oper == '//': return a//b
    elif oper == '%': return a%b
p = 1
data = list(input('Enter the expression separated by a space: ').split())
operators = ['+', '-', '*', '//', '%']
num_stack = []
for i in data:
    if i in operators:
        try:
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack.append(calc(a, b, i))
        except IndexError:
            print('invalid expression')
            p = 0
            break
    else:
        try:
            num = int(i)
        except ValueError:
            print('invalid expression')
            p = 0
            break
        finally:
            num_stack.append(num)
if len(num_stack) != 1 and p:
    print('invalid expression')
elif p:
    print(num_stack[0])
