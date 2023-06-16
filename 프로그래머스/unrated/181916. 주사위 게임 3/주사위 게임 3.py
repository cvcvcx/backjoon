def solution(a, b, c, d):
    num_list = [a,b,c,d]
    count_list = []
    answer = 0
    for n in num_list:
        count_list.append(num_list.count(n))
    if max(count_list) == 4:
        answer = a*1111
    elif max(count_list) == 3:
        p = num_list[count_list.index(3)]
        q = num_list[count_list.index(1)]
        answer = (10 * p + q) ** 2
    elif max(count_list) == 2:
        if min(count_list) == 2:
            answer = (a+c) * abs(a-c) if a == b else (a+b) * abs(a-b)
        else:
            p = num_list[count_list.index(2)]
            
            answer = a*b*c*d / p ** 2
    else:
        answer = min(num_list)
            
    return answer