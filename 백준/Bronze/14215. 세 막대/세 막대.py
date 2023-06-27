num_list = list(map(int,input().split()))

num_list.sort()
a,b,c = num_list[0],num_list[1],num_list[2]
if c >= a + b:
    c = a + b - 1
print(a+b+c)