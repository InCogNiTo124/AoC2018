recipe_scores = [int(t) for t in input()]
recipes = [3, 7]
elf_1 = 0
elf_2 = 1

i = 0
while True:
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
    if recipes[i:i+len(recipe_scores)] == recipe_scores:
        print(i)
        import sys
        sys.exit(0)
    i += 1
