#첫번째 수를 기준으로 잡으면, 첫번째 수가 등장하는게 더 많거나, 같다.
#첫번째 수를 기준으로 해서 다른 수를 뒤집는 방법으로 체크해야함
s = input()
first_num = s[0]
answer = 0
check_flag = 0
for num in s:
    if num == first_num:
        check_flag = 0
    elif num != first_num:
        if check_flag == 0:
            answer += 1
        check_flag = 1
print(answer)