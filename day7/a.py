input = [line.strip() for line in open(0).readlines() ]

def operate(stack, target, op):
    if len(stack) == 1:
        return stack[0] == target
    a = stack.pop()
    b = stack.pop()
    value = 0
    if op == '+':
        value = a + b
        if value == target:
            return True
    elif op == '*':
        value = a * b
        if value == target:
            return True
    stack.append(value)
    return operate(stack[:], target, '+') or operate(stack[:], target, '*')

sum = 0
for line in input:
    split = line.split(':')
    value = int(split[0])
    operands = [ int(x) for x in split[1].split() ]
    operands.reverse()
    if operate(operands[:], value, '+') or operate(operands[:], value, '*'):
        sum += value

print(sum)