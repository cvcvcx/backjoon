def isPrime(n):
    if n < 2:
        return False
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            return False
    return True

c = int(input())
num_list = list(map(int,input().split()))
answer = 0

for n in num_list:
    if isPrime(n):
        answer += 1
        
print(answer)