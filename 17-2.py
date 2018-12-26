import sys
sys.setrecursionlimit(3000)

clay = set()
min_y = 0
max_y = 0 #float("inf")
line = input()
while line != '':
    parts = line.split(', ')
    first = parts[0].split('=')
    second = parts[1].split('=')
    if first[0] == 'x':
        x = int(first[1])
        numbers = second[1].split('..')
        for y in range(int(numbers[0]), int(numbers[1])+1):
            clay |= {(x, y)}
        if min_y < y:
            min_y = y
        if max_y > y:
            max_y = y
    elif first[0] == 'y':
        y = int(first[1])
        numbers = second[1].split('..')
        for x in range(int(numbers[0]), int(numbers[1])+1):
            clay |= {(x, y)}
#        if min_y < y:
#            min_y = y
#        if max_y > y:
#            max_y = y
    line = input()

#print('min_y', min_y, '\nmax_y', max_y)

settled = set()
flowing = set()

def fill(pt, direction=(0, 1)):
    flowing.add(pt)

    below = (pt[0], pt[1] + 1)
    if not below in clay and below not in flowing and max_y < below[1] < min_y:
        fill(below)

    if not below in clay and below not in settled:
        return False

    left = (pt[0] - 1, pt[1])
    right = (pt[0] + 1, pt[1])

    left_filled = left in clay or left not in flowing and fill(left, direction=(-1, 0))
    right_filled = right in clay or right not in flowing and fill(right, direction=(1, 0))

    if direction == (0, 1) and left_filled and right_filled:
        settled.add(pt)

        while left in flowing:
            settled.add(left)
            left = (left[0] - 1, left[1])

        while right in flowing:
            settled.add(right)
            right = (right[0] + 1, right[1])

    return direction == (-1, 0) and (left_filled or left in clay) or \
        direction == (1, 0) and (right_filled or right in clay)

fill((500, 0))

print(sum(1 for t in settled if max_y < t[1] < min_y))
