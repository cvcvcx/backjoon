N, M = map(int,input().split())

b_list = []
for i in range(N):
    b_list.append(i+1)
for _ in range(M):
    i, j = map(int, input().split())
    i = i - 1
    j = j - 1
    b_list = b_list[:i]+b_list[i:j+1][::-1]+b_list[j+1:]
for i in range(len(b_list)):
    print(b_list[i],end = " ")