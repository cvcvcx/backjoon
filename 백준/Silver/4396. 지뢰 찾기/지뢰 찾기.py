n = int(input())
mine = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]
result = [["."] * n for _ in range(n)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for y in range(n):
    for x in range(n):
        if mine[y][x] == "." and board[y][x] == "x":
            cnt = 0
            for i in range(8):
                ny = dy[i] + y
                nx = dx[i] + x

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if mine[ny][nx] == "*":
                    cnt += 1
            result[y][x] = str(cnt)

        if mine[y][x] == "*" and board[y][x] == "x":
            for a in range(n):
                for b in range(n):
                    if mine[a][b] == "*":
                        result[a][b] = "*"
for i in range(n):
    for j in range(n):
        print(result[i][j], end="")
    print()