import sys

input = sys.stdin.readline
n = int(input().strip())
# 숫자가 들어가는 스택
stack = []
# +,- 기호가 들어가는 리스트
answer = []
# 스택으로 만들 수 있는 수열인지 판단하는 플래그
flag = 0
# 지금 스택에 들어갈 숫자
cur = 1
for _ in range(n):
    num = int(input().strip())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:        
    for i in range(len(answer)):
        print(answer[i])
            
