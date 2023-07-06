def fac(n):
    result = 1
    num = n
    while num>0:
        result = result * num
        num -= 1
    return result

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    result = fac(m)// (fac(n) * fac(m-n))
    print(result)