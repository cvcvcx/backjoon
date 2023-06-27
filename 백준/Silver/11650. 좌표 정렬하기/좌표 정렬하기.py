import sys
input = sys.stdin.readline

n = int(input())
x_y_list = []

for i in range(n):
    x,y = map(int,input().split())
    x_y_list.append((x,y))

x_y_list.sort(key = lambda x : (x[0],x[1]))

for x in x_y_list:
    print(x[0],x[1])