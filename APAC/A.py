fin = open('./A-large.in.txt', 'r')
fout = open('./A-large.out.txt', 'w')
T = int(fin.readline())
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
R = 0
C = 0
P = 0.0
Q = 0.0

def check(x, y):
    if (x<0 or y<0 or x>=R or y>=C):
        return False
    else:
        return True

def search(board, visit, x, y, remainingStep, current, maxMonster):
    if remainingStep == 0:
        maxMonster[0] = max(maxMonster[0], current)
        return
    for ii in range(4):
        nextX = x + dir[ii][0]
        nextY = y + dir[ii][1]
        if check(nextX, nextY):
            p = P if (board[nextX][nextY] == 'A') else Q
            visit[nextX][nextY] += 1
            search(board, visit, nextX, nextY, remainingStep - 1, current + pow(1 - p, visit[nextX][nextY] - 1) * p, maxMonster)
            visit[nextX][nextY] -= 1

for i in range(T):
    R, C, RS, CS, S = map(int, fin.readline().strip().split(' '))
    P, Q = map(float, fin.readline().strip().split(' '))
    board = []
    visit = []
    for r in range(R):
        board.append(fin.readline().strip().split(' '))
        visit.append([])
        for c in range(C):
            visit[r].append(0)
    maxMonster = [0.0]
    search(board, visit, RS, CS, S, 0.0, maxMonster)
    print >> fout, 'Case #%d: %s' % (i + 1, round(maxMonster[0], 7))
fin.close()
fout.close()
