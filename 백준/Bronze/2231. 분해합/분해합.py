import sys
input = sys.stdin.readline

N = int(input())
equal_numbers = []
for num in range(N):
    sum_num = num
    str_num = str(num)
    for i in range(len(str_num)):
        sum_num += int(str_num[i])
    if sum_num == N:
        equal_numbers.append(num)
if equal_numbers:
    print(min(equal_numbers))
else:
    print(0)