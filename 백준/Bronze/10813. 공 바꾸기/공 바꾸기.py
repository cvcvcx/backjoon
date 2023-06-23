N,M = map(int,input().split())

ball_list = []
for i in range(N):
    ball_list.append(i+1)
for _ in range(M):
    i, j = map(int,input().split())
    ball_list[i-1],ball_list[j-1] = ball_list[j-1], ball_list[i-1]
for i in range(N):
    print(ball_list[i],end = " ")