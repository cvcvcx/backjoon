n = int(input())
for _ in range(n):
    h,w,c = map(int,input().split())
    floor = c%h
    room = c//h +1
    if c%h == 0:
        floor = h
        room = c//h
    answer = str(floor) + format(room, "02")
    print(answer)