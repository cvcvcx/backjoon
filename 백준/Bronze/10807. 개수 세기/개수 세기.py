n = int(input())
num_list = list(map(int, input().split()))
v = int(input())
count_ = 0
if v in num_list:
    count_ = num_list.count(v)

print(count_)