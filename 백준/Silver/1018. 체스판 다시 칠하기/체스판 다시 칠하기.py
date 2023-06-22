N,M = map(int,input().split())

original_map = []
count = []

for _ in range(N):
    original_map.append(input())
    
# 8 x 8 체스판을 자를 시작부분을 정한다.
for a in range(N-7):
    for b in range(M-7):
        # 바꿔야하는 부분을 세는 count 변수를 두 개 만든다.
        # 체스판이 W로 시작하는 경우와, B로 시작하는 경우가 있기때문에 변수를 두 개 생성해야한다.
        W_start_count = 0
        B_start_count = 0
        # 체스판을 돌면서, 바꿔야하는 부분을 체크한다.
        for i in range(a,a+8):
            for j in range(b,b+8):
                #만약 좌표의 합이 짝수인 경우, 시작한 칸의 색과 같은 색이여야한다.
                if (i+j) % 2 ==0:
                    #흰색이 아니라면,
                    if original_map[i][j] != "W":
                        #W와 같아야 하는데 다르므로, W_start_count를 증가시킨다.
                        W_start_count += 1
                    #검은색이 아니라면
                    else:
                        #B와 같아야 하는데 다르므로, B_start_count를 증가시킨다.
                        B_start_count += 1
                else:
                    #좌표의 합이 홀수인 경우, 시작한 칸의 색과 다른 색이여야 한다.
                    #만약 흰 색인 경우
                    if original_map[i][j] == "W":
                        #달라야 하는데 같으므로, W_start_count를 하나 증가시킨다.
                        W_start_count += 1
                    #검은색인 경우
                    else:
                        ##달라야 하는데 같으므로, B_start_count를 하나 증가시킨다.
                        B_start_count += 1
        count.append(min(W_start_count,B_start_count))
print(min(count))
                
