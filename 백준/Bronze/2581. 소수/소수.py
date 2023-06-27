def isPrime(n):
    if n < 2:
        return False
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True

M = int(input())
N = int(input())
num_list = []

for n in range(M,N+1):
    if isPrime(n):
        num_list.append(n)
        
if num_list:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)
