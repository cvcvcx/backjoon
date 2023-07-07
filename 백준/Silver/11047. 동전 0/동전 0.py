#10 4200 
n, k = map(int,input().split())

num_list = [int(input()) for _ in range(n)]
num_list = num_list[::-1]
answer = 0
for num in num_list:
    if k // num > 0:
        answer += k//num
        k = k % num
print(answer)