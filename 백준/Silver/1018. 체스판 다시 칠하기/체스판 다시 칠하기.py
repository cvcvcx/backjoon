N, M = map(int, input().split())

original_map = [input() for _ in range(N)]

count_list = []

for start_i in range(N - 7):
    for start_j in range(M - 7):
        W_start_count = 0
        B_start_count = 0
        for i in range(start_i, start_i + 8):
            for j in range(start_j, start_j + 8):
                if (i + j) % 2 == 0:
                    if original_map[i][j] != "W":
                        W_start_count += 1
                    else:
                        B_start_count += 1
                else:
                    if original_map[i][j] == "W":
                        W_start_count += 1
                    else:
                        B_start_count += 1
        count_list.append(min(W_start_count,B_start_count))
print(min(count_list))