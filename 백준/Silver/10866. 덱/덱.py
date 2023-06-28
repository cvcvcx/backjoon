from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deque_ = deque([])

for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        deque_.appendleft(command[1])
    elif command[0] == 'push_back':
        deque_.append(command[1])
    elif command[0] == 'pop_front':
        if not deque_:
            print(-1)
        else:
            print(deque_.popleft())
    elif command[0] == 'pop_back':
        if not deque_:
            print(-1)
        else:
            print(deque_.pop())            
    elif command[0] == 'size':
        print(len(deque_))
    elif command[0] == 'empty':
        if not deque_:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not deque_:
            print(-1)
        else:
            print(deque_[0])
    elif command[0] == 'back':
        if not deque_:
            print(-1)
        else:
            print(deque_[-1])
            
    
        
    