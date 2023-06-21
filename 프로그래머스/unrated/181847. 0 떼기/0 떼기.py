def solution(n_str):
    answer = ''
    for i,n in enumerate(n_str):
        if n != "0":
            answer = n_str[i:]
            break
    return answer