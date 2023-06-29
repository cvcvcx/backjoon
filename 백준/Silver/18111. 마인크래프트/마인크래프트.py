import sys
from collections import Counter
input = sys.stdin.readline
n,m,b = map(int,input().split())
ground = []
for _ in range(n):
    ground += map(int,input().split())
#땅의 제일 낮은 위치부터, 제일 높은 위치까지 돌면서 하나하나 기준으로 삼아서 초를 센다.

min_h = min(ground)
max_h = max(ground)
sum_ = sum(ground)
ground = dict(Counter(ground))

height = 0
time = 100000000000000000

for i in range(min_h, max_h + 1):
    #지금 가지고 있는 블럭과, 땅에 있는 블럭을 모두 꺼냈을 때의 합과
    #기준으로 삼고있는 높이로 땅을 가득 채웠을 때 필요한 블럭 수를 비교해서 블럭을 놓을 수 있으면
    if sum_ + b >= i * n * m:
        #걸리는 시간 초기화
        cur_time = 0
        for key in ground:
            if key > i:
                cur_time += (key - i) * ground[key] * 2
            elif key < i:
                cur_time += (i - key) * ground[key]
        if cur_time <= time:
            time = cur_time
            height = i
            

print(time, height)
    
