from collections import deque

n, m = map(int,input().split())
my_deque = deque([])
want_num_list = list(map(int,input().split()))
count = 0

for i in range(1,n+1):
    my_deque.append(i)

for num in want_num_list:
    while True:
        if my_deque[0] == num:
            my_deque.popleft()
            break
        else:
            if my_deque.index(num) < len(my_deque)/2:
                while my_deque[0] != num:
                    my_deque.append(my_deque.popleft())
                    count += 1
            else:
                while my_deque[0] != num:
                    my_deque.appendleft(my_deque.pop())
                    count += 1
                    
print(count)