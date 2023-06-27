N, K = map(int,input().split())

counter = 0
answer = 0
for num in range(1,N+1):
    if N % num == 0:
        counter += 1
        if counter == K:
            answer = num
            break

print(answer)