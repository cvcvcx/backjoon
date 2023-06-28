import sys
input = sys.stdin.readline
def my_round(n):
    if n - int(n) >= 0.5:
        return int(n) +1
    else:
        return int(n)

n = int(input())

num_list = [int(input()) for _ in range(n)]
num_list.sort()

ignore = my_round(n*0.15)
if ignore > 0:
    num_list = num_list[ignore:-ignore]
if num_list:
    print(my_round(sum(num_list)/len(num_list)))
else:
    print(0)