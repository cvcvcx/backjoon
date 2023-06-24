N, M = map(int,input().split())
num_list_arr = []
num_list_arr2 = []
answer = []
for _ in range(N):
    num_list = list(map(int,input().split()))
    num_list_arr.append(num_list)

for _ in range(N):
    num_list = list(map(int,input().split()))
    num_list_arr2.append(num_list)

for i in range(N):
    for j in range(M):
        a = num_list_arr[i][j]+num_list_arr2[i][j]
        print(a,end=" ")
    print()
