from collections import deque

x = input().split(' ')
players_score = [0 for t in range(int(x[0]))]
marbles = int(x[6])
circle = deque()
current_player = -1
for marble in range(marbles+1):
    current_player = (current_player + 1) % len(players_score)
    if marble == 0 or marble == 1:
        circle.append(marble)
    elif marble % 23 == 0:
        players_score[current_player] += marble
        circle.rotate(7)
        players_score[current_player] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
print(max(players_score))
