import sys
input = sys.stdin.readline

K, N = map(int,input().split())

num_list = []
for _ in range(K):
    num_list.append(int(input()))
start = 1
end = max(num_list)

while start <= end:
    mid = (start+end)//2
    
    cnt = sum([n//mid for n in num_list])
    
    if cnt >= N:
        start = mid+1
    elif cnt < N:
        end = mid-1
print(end)