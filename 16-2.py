def addr(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] + before[operation[2]]
    return after

def addi(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] + operation[2]
    return after

def mulr(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] * before[operation[2]]
    return after

def muli(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] * operation[2]
    return after

def banr(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] & before[operation[2]]
    return after

def bani(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] & operation[2]
    return after

def borr(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] |  before[operation[2]]
    return after

def bori(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]] |  operation[2]
    return after

def setr(operation, before):
    after = before.copy()
    after[operation[3]] = before[operation[1]]
    return after

def seti(operation, before):
    after = before.copy()
    after[operation[3]] = operation[1]
    return after

def gtir(operation, before):
    after = before.copy()
    after[operation[3]] = int(operation[1] > before[operation[2]])
    return after

def gtri(operation, before):
    after = before.copy()
    after[operation[3]] = int(before[operation[1]] > operation[2])
    return after

def gtrr(operation, before):
    after = before.copy()
    after[operation[3]] = int(before[operation[1]] > before[operation[2]])
    return after

def eqir(operation, before):
    after = before.copy()
    after[operation[3]] = int(operation[1] == before[operation[2]])
    return after

def eqri(operation, before):
    after = before.copy()
    after[operation[3]] = int(before[operation[1]] == operation[2])
    return after

def eqrr(operation, before):
    after = before.copy()
    after[operation[3]] = int(before[operation[1]] == before[operation[2]])
    return after

functions = dict({
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
})
op_codes_temp = dict()

while True:
    before = input()
    if before == '':
        break
    operation = input()
    after = input()
    input()
    before = [int(t) for t in before[9:-1].split(', ')]
    operation = [int(t) for t in operation.split()]
    after = [int(t) for t in after[9:-1].split(', ')]
    if operation[0] in op_codes_temp:
        op_codes_temp[operation[0]] &= set([op for op in functions if functions[op](operation, before) == after])
    else:
        op_codes_temp[operation[0]] = set([op for op in functions if functions[op](operation, before) == after])

op_codes = dict()
while len(op_codes_temp) > 0:
    op_codes.update({key: list(op_codes_temp[key])[0] for key in op_codes_temp if len(op_codes_temp[key]) == 1})
    for key in op_codes:
        op_codes_temp.pop(key, None)
    unq_vals = set([t for t in op_codes.values()])
    for key in op_codes_temp:
        op_codes_temp[key] -= unq_vals

line = input()
line = input()
registers = [0, 0, 0, 0]
while line != '':
    operation = [int(t) for t in line.split(' ')]
    registers = functions[op_codes[operation[0]]](operation, registers)
    line = input()
print(registers)
