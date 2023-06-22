def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


i, j = map(int, input().split())

for num in range(i, j + 1):
    if isPrime(num):
        print(num)
