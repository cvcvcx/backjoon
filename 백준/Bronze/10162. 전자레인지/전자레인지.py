second_list = [300,60,10]
t = int(input())
answer_list = []
for s in second_list:
    answer_list.append(t//s)
    t = t % s
if t > 0:
    print(-1)
else:
    print(*answer_list)