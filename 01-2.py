X = []
x = input()
while x != "":
    X.append(int(x))
    x = input()

a = [0]
i = 0
s = X[i]
while s not in a:
    a.append(s)
    i = (i + 1) % len(X)
    s += X[i]
print(s)
