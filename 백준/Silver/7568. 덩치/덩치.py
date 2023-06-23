import sys
input = sys.stdin.readline

n = int(input().strip())

man_list = []

for i in range(n):
    x, y = map(int,input().split())
    man_list.append((x,y))
for man in man_list:
    rank = 1
    for l in man_list:
        if man[0] < l[0] and man[1] < l[1]:
            rank += 1
    print(rank,end=" ")