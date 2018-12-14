#from collections import deque

repetitions = int(input())
recipes = [3, 7]
elf_1 = 0
elf_2 = 1

while len(recipes) < repetitions + 10:
    x = recipes[elf_1]
    y = recipes[elf_2]
    s = x + y
    if s < 10:
        recipes.append(s)
    else:
        recipes.append(s // 10)
        recipes.append(s % 10)
    elf_1 = (elf_1 + 1 + x)%len(recipes)
    elf_2 = (elf_2 + 1 + y)%len(recipes)

print("".join([str(t) for t in recipes[repetitions:repetitions+10]]))
