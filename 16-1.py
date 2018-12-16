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

ambiguous = 0
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
    ambiguous += int(sum((functions[op](operation, before) == after for op in functions)) >= 3)

print(ambiguous)
