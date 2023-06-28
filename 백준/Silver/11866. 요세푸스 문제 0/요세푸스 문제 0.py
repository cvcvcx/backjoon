from collections import deque

queue = deque([])
answer = []
n, k = map(int,input().split())
for i in range(1,n+1):
    queue.append(i)
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
print_answer = "<"
for num in answer:
    print_answer += str(num) + ", "
print(print_answer[:-2] + ">")