import sys
input = sys.stdin.readline
n = int(input())

num_list = [int(input()) for _ in range(n)]
num_list.sort()
num_count_dict = {}
aver = round(sum(num_list)/len(num_list))
center = num_list[len(num_list)//2]
mode = 0
range_num = 0
for num in num_list:
    if num in num_count_dict:
        num_count_dict[num] += 1
    else:
        num_count_dict[num] = 1
        
max_count = max(num_count_dict.values())
max_num_list = []

for key, value in num_count_dict.items():
    if value == max_count:
        max_num_list.append(key)
if len(max_num_list)>1:
    max_num_list.sort()
    mode = max_num_list[1]
else:
    mode = max_num_list[0]
    
range_num = abs(max(num_list)-min(num_list))

print(aver)
print(center)
print(mode)
print(range_num)
