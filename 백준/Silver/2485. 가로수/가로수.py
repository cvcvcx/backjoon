import sys
input = sys.stdin.readline
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

n = int(input())


num_list = [int(input().strip()) for _ in range(n)]
min_ = min(num_list)
max_ = max(num_list)
min_gcd = 1000000000000

for i in range(1,len(num_list)-1):
    gcd_ = gcd(num_list[i]-min_,num_list[i+1]-min_)
    if gcd_ < min_gcd:
        min_gcd = gcd_
print((max_ - min_) // min_gcd  + 1 - len(num_list))