t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    f0_list = [x for x in range(1,n+1)]
    for f in range(k):
        for i in range(1,n):
            f0_list[i] += f0_list[i-1]
    print(f0_list[-1])