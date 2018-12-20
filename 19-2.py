import time

def addr(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] + before[operation[1]]
    return after

def addi(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] + operation[1]
    return after

def mulr(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] * before[operation[1]]
    return after

def muli(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] * operation[1]
    return after

def banr(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] & before[operation[1]]
    return after

def bani(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] & operation[1]
    return after

def borr(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] |  before[operation[1]]
    return after

def bori(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]] |  operation[1]
    return after

def setr(operation, before):
    after = before.copy()
    after[operation[2]] = before[operation[0]]
    return after

def seti(operation, before):
    after = before.copy()
    after[operation[2]] = operation[0]
    return after

def gtir(operation, before):
    after = before.copy()
    after[operation[2]] = int(operation[0] > before[operation[1]])
    return after

def gtri(operation, before):
    after = before.copy()
    after[operation[2]] = int(before[operation[0]] > operation[1])
    return after

def gtrr(operation, before):
    after = before.copy()
    after[operation[2]] = int(before[operation[0]] > before[operation[1]])
    return after

def eqir(operation, before):
    after = before.copy()
    after[operation[2]] = int(operation[0] == before[operation[1]])
    return after

def eqri(operation, before):
    after = before.copy()
    after[operation[2]] = int(before[operation[0]] == operation[1])
    return after

def eqrr(operation, before):
    after = before.copy()
    after[operation[2]] = int(before[operation[0]] == before[operation[1]])
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

registers = [0 for i in range(6)]
registers[0] = 1
ip = int(input().split(' ')[1])
commands = []
line = input()
while line != '':
    parts = line.split(' ')
    commands.append((parts[0], [int(t) for t in parts[1:]]))
    line = input()
#print("\n".join([repr(t) for t in commands]))
#done = False
while True:
    try:
        command, abc = commands[registers[ip]]
    except:
        break
    print("ip = ", registers[ip], registers, command, abc, end=' ')
    registers = functions[command](abc, registers)
#    if not done and registers[ip] == 3 and registers[4] == 10551347:
#        registers[5] = registers[4]
#        registers[2] = registers[4]
#        done = True
#        print('/n'*10)
    print(registers)
    registers[ip] += 1
    time.sleep(1)

print(registers)
