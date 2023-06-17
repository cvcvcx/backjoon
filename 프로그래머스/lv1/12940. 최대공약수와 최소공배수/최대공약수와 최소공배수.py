def solution(n, m):
    return [gcd(n,m),lcm(n,m)]

def gcd(x,y):
    while y>0:
        x, y = y, x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)