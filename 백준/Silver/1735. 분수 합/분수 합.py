import sys
input = sys.stdin.readline

def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
def lcm(x,y):
    return x*y // gcd(x,y)

n1,d1 = map(int,input().split())
n2,d2 = map(int,input().split())

sum_ = n1 * d2 + n2 * d1
d_mul = d1 * d2
gcd_ = gcd(sum_,d_mul)
print(sum_//gcd_, d_mul//gcd_)