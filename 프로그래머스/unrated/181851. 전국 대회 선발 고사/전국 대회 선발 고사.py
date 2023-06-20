def solution(rank, attendance):
    answer = 0
    answer_list = []
    rank_idx = {e:i for i,e in enumerate(rank)}
    for i in range(len(attendance)):
        if attendance[i] == True:
            answer_list.append(rank[i])
    answer_list.sort()
    a,b,c = answer_list[:3]
    answer = rank_idx[a]*10000+rank_idx[b]*100+rank_idx[c]
    return answer