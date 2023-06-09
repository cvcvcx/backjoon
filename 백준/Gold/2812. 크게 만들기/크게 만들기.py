n, k = map(int,input().split())
number_list = list(input())
stack = []
cnt = k

for num in number_list:
    while stack and num>stack[-1] and cnt>0:
        stack.pop()
        cnt -= 1
    stack.append(num)
print(''.join(stack[:n-k]))