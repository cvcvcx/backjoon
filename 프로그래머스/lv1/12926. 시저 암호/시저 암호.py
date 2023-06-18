def solution(s, n):
    answer = ''
    lower_al = 'abcdefghijklmnopqrstuvwxyz'
    upper_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    al_index = 0
    for c in s:
        if c in lower_al:
            if lower_al.index(c) + n < 25:
                al_index = lower_al.index(c) + n
            else:
                al_index = lower_al.index(c) + n - 26
            answer += lower_al[al_index]
        elif c in upper_al:
            if upper_al.index(c) + n < 25:
                al_index = upper_al.index(c) + n
            else:
                al_index = upper_al.index(c) + n - 26
            answer += upper_al[al_index]
        else:
            answer += " "
    return answer