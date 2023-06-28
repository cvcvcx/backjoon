from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    while queue:
        max_num = max(queue)
        if queue[0] == max_num:
            queue.popleft()
            if m == 0:
                cnt += 1
                break
            else:
                cnt += 1
                m -= 1
        else:
            a = queue.popleft()
            queue.append(a)
            if m == 0:
                m += len(queue) - 1
            else:
                m -= 1
    print(cnt)