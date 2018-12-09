<<<<<<< Updated upstream
from collections import deque

x = input().split(' ')
players_score = [0 for t in range(int(x[0]))]
marbles = int(x[6])
circle = deque()
=======
x = input().split(' ')
players_score = [0 for t in range(int(x[0]))]
marbles = int(x[6])
circle = []
current_marble_index = 0
>>>>>>> Stashed changes
current_player = -1
for marble in range(marbles+1):
    current_player = (current_player + 1) % len(players_score)
    if marble == 0 or marble == 1:
        circle.append(marble)
<<<<<<< Updated upstream
    elif marble % 23 == 0:
        players_score[current_player] += marble
        circle.rotate(7)
        players_score[current_player] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
=======
        current_marble_index = marble
    elif marble % 23 == 0:
        players_score[current_player] += marble
        delete_index = (current_marble_index - 7) % len(circle)
        players_score[current_player] += circle[delete_index]
        del(circle[delete_index])
        current_marble_index = delete_index % len(circle)
    else:
        current_marble_index = (current_marble_index + 1) % len(circle)+1
        circle.insert(current_marble_index, marble)
>>>>>>> Stashed changes
print(max(players_score))
