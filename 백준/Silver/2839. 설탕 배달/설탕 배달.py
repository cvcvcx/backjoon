N = int(input())

count = -1
minus_num = -3
answer_list = []
while minus_num < N:
    count += 1
    minus_num += 3
    if (N - minus_num) % 5 == 0:
        answer_list.append(count + (N-minus_num)//5)
if answer_list:
    print(min(answer_list))
else:
    print(-1)