
from collections import deque
from typing import List
def move_obstacle(lot):
    # WRITE YOUR BRILLIANT CODE HERE
    num_rows = len(lot)
    # return 0
    num_cols = len(lot[0])
    def get_neighbors(coord):
        row, col = coord
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            r = row + dx
            c = col + dy
            if 0 <= r < num_rows and 0 <= c < num_cols:
                yield (r, c)
    def bfs(start):
        queue = deque([start])
        r, c = start
        lot[r][c] = 0
        dist = 0
        while len(queue) > 0:
            dist += 1
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for r, c in get_neighbors(node):
                    if lot[r][c] == 9:
                        return dist
                    if lot[r][c] == 0:
                        continue
                    queue.append((r, c))
                    lot[r][c] = 0
    return bfs((0, 0))


if __name__ == '__main__':
    # lot = [[int(x) for x in input().split()] for _ in range(int(input()))]
    area1= [
    [1,0,0],
    [1,0,0],
    [1,9,1]
    ]
    area2 = [
        [1,1,1],
        [1,0,1],
        [0,1,9]
    ]
    area3 = [
        [1,0,0],
        [1,0,0],
        [1,9,1]
    ]
    res = move_obstacle(area1)
    print(res)

    res = move_obstacle(area2)
    print(res)

    res = move_obstacle(area3)
    print(res)
