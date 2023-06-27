def lcm(x,y):
    while y>0:
        x,y = y,x
        y = y%x
    return x

def gcd(x,y):
    return (x*y)//lcm(x,y)

x, y = map(int,input().split())
print(lcm(x,y))
print(gcd(x,y))