# Link: https://www.acmicpc.net/source/40824953

from queue import Queue

# use dx & dy to check adjacent cells (left, right, down, up)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())                                    # GOAL: (1, 1) -> (M, N) where M: colm(x), N: row(y)
board = []


# to check if x & y are in the range of cells
def isRange(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:                          # when out of range -> return false
        return False
    return True


# [x, y, dist]
def BFS():
    visited = [[False for col in range(M)] for row in range(N)]     # create list of cells filled with False
    queue = Queue()                                                 # create a queue
    queue.put([0, 0, 1])                                            # put the 1st cell (start pt) into the queue
    visited[0][0] = True                                            # False -> True b/c already checked

    while queue.qsize() > 0:                                        # repeat this step while queue isn't empty
        now = queue.get()                                           # use .get() to the 1st data in the queue
        x = now[0]
        y = now[1]
        dist = now[2]

        if x == M - 1 and y == N - 1:                               # using index (0,0). GOAL: (O,0) -> (M-1, N-1)
            return dist                                             # when we reached goal -> return dist

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if not isRange(nextX, nextY):                           # not in the range of cells -> skip
                continue

            elif visited[nextY][nextX]:                             # if already visited -> skip
                continue

            elif board[nextY][nextX] == 0:                          # if 0: not a path -> skip
                continue

            # to denote the cells that's already been visited: False -> True
            visited[nextY][nextX] = True                            # above 3 conditions not applied -> path
            queue.put([nextX, nextY, dist + 1])                     # add our newly visited cell to queue & +1 to dist

    return -1                                                       # not applied to any: can't reach goal -> return -1


if __name__ == '__main__':
    for i in range(N):
        board.append(list(map(int, str(input()))))

    result = BFS()
    print(result)

