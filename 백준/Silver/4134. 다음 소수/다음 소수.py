def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    check_num = num
    while isPrime(check_num) == False:
        check_num += 1
    print(check_num)