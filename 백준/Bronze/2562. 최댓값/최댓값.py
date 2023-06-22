num_list = {}
for i in range(9):
    num_list[int(input())] = i
max_number = max(list(num_list.keys()))
max_idx = num_list[max_number] + 1
print(max_number)
print(max_idx)