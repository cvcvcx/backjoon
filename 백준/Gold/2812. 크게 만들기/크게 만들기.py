n, k = map(int,input().split())
number = list(input())

answer = []
cnt = k
for num in number:
    while answer and cnt>0 and num>answer[-1]:
        del answer[-1]
        cnt -=1
    answer.append(num)
print(''.join(answer[:n-k]))
        