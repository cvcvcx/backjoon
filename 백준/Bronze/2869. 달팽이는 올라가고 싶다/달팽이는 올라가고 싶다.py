A, B, V = map(int,input().split())

day = 1
snail_one_day = A-B
goal = V - A

if goal % snail_one_day:
    day += goal//snail_one_day + 1
else:
    day += goal//snail_one_day


print(day)