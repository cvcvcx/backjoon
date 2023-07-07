n = int(input())
num_list = list(map(int,input().split()))

num_list.sort()
answer = 0
tmp_sum = 0
for num in num_list:
    tmp_sum += num
    answer += tmp_sum
print(answer)