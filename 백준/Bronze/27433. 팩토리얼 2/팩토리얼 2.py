def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return n * 1
    else:
        return n * fac(n-1)
n = int(input())
print(fac(n))