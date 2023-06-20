def solution(survey, choices):
    dict_ = {t:0 for t in "RTCFJMAN"}
    for i,c in enumerate(choices):
        if c > 4:
            dict_[survey[i][1]] += (c - 4)
        elif c < 4:
            dict_[survey[i][0]] += (4 - c)
    mbti = ""
    values = list(dict_.values())
    keys = list(dict_.keys())
    for i in range(0,len(values),2):
        if values[i] > values[i+1]:
            mbti += keys[i]
        elif values[i] < values[i+1]:
            mbti += keys[i+1]
        else:
            tmp = [keys[i],keys[i+1]]
            tmp.sort()
            mbti += tmp[0]
    return mbti