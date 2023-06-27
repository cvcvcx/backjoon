while True:
    num_list = list(map(int,input().split()))
    num_list.sort()
    if num_list[-1] == 0:
        break
    a,b,c = num_list[0],num_list[1],num_list[2]
    if c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")

