line_num = 0
idx_num = 0
num_list_arr = []
max_num_list = []
max_num_idx_list = []
for i in range(9):
    tmp = list(map(int,input().split()))
    num_list_arr.append(tmp)
    max_num_list.append(max(tmp))
    max_num_idx_list.append(tmp.index(max(tmp)))
final_max_num = max(max_num_list)
line_num = max_num_list.index(final_max_num)
idx_num = max_num_idx_list[line_num]

print(final_max_num)
print(line_num+1,idx_num+1)