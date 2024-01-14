import re
from queue import Queue

input = open('input2.txt').read().splitlines()

bf = []
ops = []
af = []
operations = []
program = []
for line in input:
    if line == '':
        continue
    if line.startswith('Before'):
        bf = [int(x) for x in re.findall(r'\d+', line)]
    elif line[0].isnumeric():
        if bf == []:
            program.append([int(x) for x in line.split(' ')])
            continue
        ops = [int(x) for x in line.split(' ')]
    elif line.startswith('After'):
        af = [int(x) for x in re.findall(r'\d+', line)]
        operations.append((bf, ops, af))
        bf, ops, af = [], [], []

def addr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]

def addi(registers, A, B, C):
    registers[C] = registers[A] + B

def mulr(registers, A, B, C):
    registers[C] = registers[A] * registers[B]

def muli(registers, A, B, C):
    registers[C] = registers[A] * B

def banr(registers, A, B, C):
    registers[C] = registers[A] & registers[B]

def bani(registers, A, B, C):
    registers[C] = registers[A] & B

def borr(registers, A, B, C):
    registers[C] = registers[A] | registers[B]

def bori(registers, A, B, C):
    registers[C] = registers[A] | B

def setr(registers, A, B, C):
    registers[C] = registers[A]

def seti(registers, A, B, C):
    registers[C] = A

def gtir(registers, A, B, C):
    if A > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def gtri(registers, A, B, C):
    if registers[A] > B:
        registers[C] = 1
    else:
        registers[C] = 0

def gtrr(registers, A, B, C):
    if registers[A] > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def eqir(registers, A, B, C):
    if A == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def eqri(registers, A, B, C):
    if registers[A] == B:
        registers[C] = 1
    else:
        registers[C] = 0

def eqrr(registers, A, B, C):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

possible_operations = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}

possible_opcodes = [None for _ in range(16)]
for before, ops, after in operations:
    actions = set()
    for op_name, operation in possible_operations.items():
        registers_copy = list(before)
        operation(registers_copy, ops[1], ops[2], ops[3])
        if registers_copy == after:
            actions.add(op_name)
    if possible_opcodes[ops[0]] == None:
        possible_opcodes[ops[0]] = actions
    else:
        possible_opcodes[ops[0]] &= actions

opcodes = [None for _ in range(16)]
Q = Queue()
for i in range(16):
    Q.put(i)

while Q.empty() == False:
    idx = Q.get()
    if len(possible_opcodes[idx]) == 1:
        code = possible_opcodes[idx].pop()
        opcodes[idx] = possible_operations[code]
        for s in possible_opcodes:
            if code in s:
                s.remove(code)
    else:
        Q.put(idx)

registers = [0, 0, 0, 0]
for op, A, B, C in program:
    opcodes[op](registers, A, B, C)

print(registers[0])