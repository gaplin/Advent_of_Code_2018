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

input = open('input2.txt').read().splitlines()
ip_register = int(input[0].split(' ')[1])
program = []
for line in input[1:]:
    line = line.split(' ')
    operation = line[0]
    nums = [int(x) for x in line[1:]]
    program.append((operation, nums))

ip = 0
registers = [0 for _ in range(6)]
registers[0] = 1
n = len(program)
i = 0
while 0 <= ip < n and i < 1000:
    i += 1
    registers[ip_register] = ip
    operation, nums = program[ip]
    possible_operations[operation](registers, nums[0], nums[1], nums[2])
    ip = registers[ip_register]
    ip += 1

num = registers[2]

result = 0
i = 1
while i * i <= num:
    if num % i == 0:
        result += i
        if i * i != num:
            result += num // i
    i += 1

print(result)