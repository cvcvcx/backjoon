import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))

for b in B:
    #인덱스를 탐색하는 경우에는 0부터 시작하게끔 할 것
    #자연수를 탐색하는 경우에는 1부터 시작하게
    start = 0
    end = len(A) - 1
    flag = 0
    
    while start <= end:
        mid = (start + end) // 2
        if b == A[mid]:
            flag = 1
            print(1)
            break
        elif b > A[mid]:
            start = mid + 1
        else:
            end = mid - 1            
    if flag != 1:
        print(0)
    