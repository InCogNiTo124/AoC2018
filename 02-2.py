def diff(a, b):
    s = 0
    for x, y in zip(a, b):
        if x != y:
            s += 1
    return s

x = []
diff_min = float("inf")
a = ''
b = ''
while True:
    try:
        x.append(input().strip(' ').strip('\n'))
    except:
        break
x.remove('')
for i in range(len(x) - 1):
    for j in range(i+1, len(x)):
        t = diff(x[i], x[j])
        if t < diff_min:
            diff_min = t
            print(diff_min)
            a = x[i]
            print(a)
            b = x[j]
            print(b)

print(diff_min)
print(a)
print(b)
# print(diff("abc", "abd"))
