n = int(input())
x_list = []
y_list = []
arr = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
rect = 0
for idx in range(len(arr)):
    rect += sum(arr[idx])

print(rect)