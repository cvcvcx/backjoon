num_list_arr = [list(map(int,input().split())) for _ in range(9)]
v, a = 0, [0,0]
for i in range(9):
    for j in range(9):
        if num_list_arr[i][j] >= v:
            v = num_list_arr[i][j]
            a = [i+1,j+1]
print(v)
print(*a)