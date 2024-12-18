registers = { 'A': 0, 'B': 0, 'C': 0 }
output = []

input = open("input.txt").read().split("\n\n")
reg_init = [ line for line in input[0].split('\n') ]
for init in reg_init:
    reg = init[init.index(' ')+1:init.index(':')]
    val = int(init[init.index(':')+2:])
    registers[reg] = val
program = [ int(val) for val in input[1][input[1].index(' ')+1:].split(',') ]

def get_combo_val(operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']    
    return None

ip = 0
while True:
    if ip >= len(program):
        break
    opcode = program[ip]
    if opcode == 0: # adv
        operand = get_combo_val(program[ip + 1])
        denom = 2 ** operand
        registers['A'] //= denom
    elif opcode == 1: # bxl
        operand = program[ip + 1]
        registers['B'] ^= operand
    elif opcode == 2: # bst
        operand = get_combo_val(program[ip + 1]) % 8
        registers['B'] = operand
    elif opcode == 3: # jnz
        a_val = registers['A']
        if a_val != 0:
            operand = program[ip + 1]
            ip = operand
            continue
    elif opcode == 4: # bxc
        registers['B'] ^= registers['C']
    elif opcode == 5: # out
        operand = get_combo_val(program[ip + 1]) % 8
        output.append(str(operand))
    elif opcode == 6: # bdv
        operand = get_combo_val(program[ip + 1])
        denom = 2 ** operand
        registers['B'] = registers['A'] // denom
    elif opcode == 7: # cdv
        operand = get_combo_val(program[ip + 1])
        denom = 2 ** operand
        registers['C'] = registers['A'] // denom
    ip += 2

print(','.join(output))