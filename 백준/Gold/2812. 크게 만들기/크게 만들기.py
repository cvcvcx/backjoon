N, K = map(int,input().split())
number_list = list(input())
stack = []
cnt = K
for num in number_list:
    while stack and num>stack[-1] and cnt>0:
        del stack[-1]
        cnt -= 1
    stack.append(num)
print(''.join(stack[:N-K]))
    
    