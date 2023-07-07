import sys
from collections import deque

#첫째 줄에 테스트케이스 T가 주어진다.
t = int(input().rstrip())
#각 테스트케이스의 첫째 줄에는 수행할 함수가 주어진다.
for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    num_str_arr = input().rstrip()[1:-1].split(",")
    num_deque = deque(num_str_arr)
    r_count = 0
    is_error = False
    if n == 0:
        num_deque = []
    for c in p:
        if c == "R":
            r_count += 1
        else:
            if num_deque:
                if r_count % 2 == 1:
                    num_deque.pop()
                else:
                    num_deque.popleft()
            else:
                is_error = True
                break
    if is_error:
        print('error')
    else:
        if r_count % 2 == 1:
            num_deque.reverse()
            print("[" + ','.join(num_deque) + "]")
        else:
            print("[" + ','.join(num_deque) + "]")
