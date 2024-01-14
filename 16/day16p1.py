import re

input = open('input2.txt').read().splitlines()

bf = []
ops = []
af = []
operations = []
for line in input:
    if line == '':
        continue
    if line.startswith('Before'):
        bf = [int(x) for x in re.findall(r'\d+', line)]
    elif line[0].isnumeric():
        if bf == []:
            break
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

possible_operations = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
]

result = 0
for before, ops, after in operations:
    possible_count = 0
    for operation in possible_operations:
        registers_copy = list(before)
        operation(registers_copy, ops[1], ops[2], ops[3])
        if registers_copy == after:
            possible_count += 1
    if possible_count >= 3:
        result += 1

print(result)