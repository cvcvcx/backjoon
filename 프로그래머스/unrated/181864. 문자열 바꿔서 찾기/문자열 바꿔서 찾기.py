def solution(myString, pat):
    answer = 0
    tmp_s = ""
    for s in myString:
        if s == "A":
            tmp_s += "B"
        else:
            tmp_s += "A"
    if pat in tmp_s:
        answer = 1
    return answer