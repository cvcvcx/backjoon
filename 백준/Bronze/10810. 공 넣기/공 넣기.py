N, M = map(int,input().split())
result = [0] * N
for _ in range(M):
    i, j, k = map(int,input().split())
    for n in range(i-1,j):
        result[n] = k
for r in result:
    print(r,end=" ")