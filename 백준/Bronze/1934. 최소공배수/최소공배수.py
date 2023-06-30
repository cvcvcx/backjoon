def gcd(x,y):
    while y>0:
        x,y = y,x
        y = y % x
    return x
def lcm(x,y):
    return x*y // gcd(x,y)

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    print(lcm(x,y))
