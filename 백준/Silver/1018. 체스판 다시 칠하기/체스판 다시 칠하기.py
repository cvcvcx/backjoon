N,M = map(int,input().split())

original_map = []
count = []

for _ in range(N):
    original_map.append(input())
    

for a in range(N-7):
    for b in range(M-7):
        W_start_index = 0
        B_start_index = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 ==0:
                    if original_map[i][j] != "W":
                        W_start_index += 1
                    else:
                        B_start_index += 1
                else:
                    if original_map[i][j] == "W":
                        W_start_index += 1
                    else:
                        B_start_index += 1
        count.append(min(W_start_index,B_start_index))
print(min(count))
                
