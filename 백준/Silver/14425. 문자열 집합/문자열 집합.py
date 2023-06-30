n,m = map(int,input().split())
S = {input():0 for _ in range(n)}
answer = 0
for _ in range(m):
    check_string = input()
    if check_string in S:
        answer += 1
print(answer)