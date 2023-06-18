def solution(k, score):
    answer = []
    score_list = []
    for i,n in enumerate(score):
        if i<k:
            score_list.append(n)
        elif len(score_list)>0 and min(score_list)<n:
            score_list[score_list.index(min(score_list))] = n
        answer.append(min(score_list))
    return answer