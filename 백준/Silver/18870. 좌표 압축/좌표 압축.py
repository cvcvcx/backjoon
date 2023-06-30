import sys
input = sys.stdin.readline
n = int(input())

num_list = list(map(int,input().split()))
num_set_list = list(set(num_list))
num_set_list.sort()
num_idx_dict = {num:i for i,num in enumerate(num_set_list)}
for num in num_list:
    print(num_idx_dict[num],end=" ")