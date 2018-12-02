s = 1
remember = dict()
while True:
    try:
        x = sorted(list(input()))
    except:
        break
    d = dict()
    for c in x:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if 2 in d.values():
        remember[2] = 1 if 2 not in remember else remember[2] + 1

    if 3 in d.values():
        remember[3] = 1 if 3 not in remember else remember[3] + 1
    del(d)

for t in remember.values():
    s *= t
print(remember)
print(s)
