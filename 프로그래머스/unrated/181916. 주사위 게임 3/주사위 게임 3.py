def solution(a, b, c, d):
    answer = 0
    number_list = [a,b,c,d]
    count_list = []
    
    for i in number_list:
        count_list.append(number_list.count(i))
    
    if max(count_list) == 4:
        answer = a * 1111
    elif max(count_list) == 3:
        answer = (10 *number_list[count_list.index(3)] + number_list[count_list.index(1)]) ** 2
    elif max(count_list) == 2:
        if min(count_list) == 2:
            answer = (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = number_list[count_list.index(2)]
            answer = (a*b*c*d)/p**2
    else:
        answer = min(number_list)
    return answer